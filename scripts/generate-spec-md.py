#!/usr/bin/env python3
# AUTHORED-BY Claude Fable
"""Generate the human-readable UC&R spec markdown from the machine-readable
lws-ucr corpus (ucr/*.ttl + vocab/ + vocab/schemes/).

Outputs (overwritten in place):
  spec/user-stories.md        — use cases, grouped by story group / category
  spec/requirements.md        — requirements with generated traceability
  spec/requirements-matrix.md — generated use-case -> requirements table

The Turtle corpus is the source of truth; these files are BUILD ARTIFACTS.
Run `--check` to verify the committed markdown matches the corpus (exit 1 on
drift) without writing.

Requires rdflib (installed with pyshacl).
"""

import sys
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef
from rdflib.collection import Collection

ROOT = Path(__file__).resolve().parent.parent

LWS_UCR = Namespace("https://jeswr.org/ns/lws-ucr#")
ROLE = Namespace("https://jeswr.org/ns/lws-ucr/roles#")
CAT = Namespace("https://jeswr.org/ns/lws-ucr/categories#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
OSLC_RM = Namespace("http://open-services.net/ns/rm#")

GENERATED_NOTE = (
    "<!-- GENERATED from ucr/*.ttl by scripts/generate-spec-md.py — DO NOT EDIT BY HAND.\n"
    "     Edit the Turtle corpus and regenerate (python3 scripts/generate-spec-md.py). -->\n"
)

# Story-group layout of the document: (group heading, [category IRIs in order]).
GROUPS = [
    ("Functional Stories", [CAT.DataManagement, CAT.AccessControlSharing,
                            CAT.CollaborationCommunication, CAT.ApplicationIntegration,
                            CAT.AdvancedFeatures]),
    ("Non-Functional Stories", [CAT.SecurityPrivacy, CAT.PerformanceUsability]),
    ("Technical Stories", [CAT.IdentityAuthenticationTrust, CAT.ApiProtocolFlexibility,
                           CAT.StorageResourceManagement]),
]
CATEGORY_ORDER = [c for _, cats in GROUPS for c in cats]

PRIORITY_ORDER = [LWS_UCR.Must, LWS_UCR.Should, LWS_UCR.Could, LWS_UCR.Wont]
STATUS_ORDER = [LWS_UCR.Accepted, LWS_UCR.Proposed, LWS_UCR.Deferred,
                LWS_UCR.OutOfScope, LWS_UCR.Superseded]
SCENARIO_KIND_ORDER = [LWS_UCR.MainFlow, LWS_UCR.AlternativeFlow, LWS_UCR.ErrorFlow]
SCENARIO_KIND_LABEL = {LWS_UCR.MainFlow: "Main flow", LWS_UCR.AlternativeFlow: "Alternative flow",
                       LWS_UCR.ErrorFlow: "Error flow"}


def load_graph() -> Graph:
    g = Graph()
    for f in [ROOT / "vocab" / "lws-ucr.ttl", *sorted((ROOT / "vocab" / "schemes").glob("*.ttl")),
              *sorted((ROOT / "ucr").glob("*.ttl"))]:
        g.parse(f, format="turtle")
    return g


def one(g, s, p):
    for o in g.objects(s, p):
        return o
    return None


def text(g, s, p):
    o = one(g, s, p)
    return str(o) if o is not None else None


def texts(g, s, p):
    return sorted(str(o) for o in g.objects(s, p))


def label(g, concept):
    return text(g, concept, SKOS.prefLabel) or str(concept).rsplit("#", 1)[-1]


def anchor(ident: str) -> str:
    return ident.lower()


# Words beginning with a vowel LETTER but a consonant SOUND ("a user", "a
# European"). EXACT exceptions only — a broad `uni`/`use`/`eu` prefix rule is
# wrong for the vowel-sounding negation words ("an unidentified user", "an
# uninsured patient", "an unusable pod"): "uni-" is only consonant-sounding
# ("yoo") for the Latin one-root, not for "un-" + i… . Anything not listed
# falls through to the vowel-letter default, which is correct for those.
_CONSONANT_SOUND = {"user", "users", "usual", "usable", "useful", "useless",
                    "usage", "use", "used", "utility", "utilities",
                    "european", "euro", "eulogy", "one", "once", "ubiquitous",
                    "unicorn", "unit", "units", "unified", "uniform", "union",
                    "unique", "unilateral", "unison", "universal", "universe",
                    "university", "universities"}
# Words beginning with a consonant LETTER but a vowel SOUND ("an hour", "an honest")
_VOWEL_SOUND = {"hour", "honest", "heir", "honour", "honor", "honorary"}


def indefinite_article(noun_phrase: str) -> str:
    """'a' or 'an' for a noun phrase, exception-aware (a plain vowel-letter
    heuristic gives the wrong result for 'user', 'hour', etc.).

    Consonant-sounding vowel-letter words (the exact-exception set):

    >>> [indefinite_article(p) for p in ("user", "university", "unique unit",
    ...                                  "european auditor", "one shared pod")]
    ['a', 'a', 'a', 'a', 'a']

    Vowel-sounding "un-" negation words must NOT be caught by a `uni` prefix
    rule (the bug this test pins down):

    >>> [indefinite_article(p) for p in ("unidentified user", "uninsured patient",
    ...                                  "unusual actor", "unauthorized agent")]
    ['an', 'an', 'an', 'an']

    Plain vowel/consonant defaults and the silent-h exceptions:

    >>> (indefinite_article("administrator"), indefinite_article("application developer"),
    ...  indefinite_article("hour"), indefinite_article("data owner"))
    ('an', 'an', 'an', 'a')
    """
    word = noun_phrase.strip().split()[0].lower().strip(".,;:")
    if word in _VOWEL_SOUND:
        return "an"
    if word in _CONSONANT_SOUND:
        return "a"
    return "an" if word and word[0] in "aeiou" else "a"


def source_link(url: str) -> str:
    """Render a source IRI as a short markdown link."""
    u = str(url)
    if "/issues/" in u:
        return f"[#{u.rsplit('/', 1)[-1]}]({u})"
    if u.startswith("https://github.com/"):
        return f"[{u.removeprefix('https://github.com/').removesuffix('/')}]({u})"
    return f"[{u}]({u})"


def source_sort_key(u: str):
    # issues numerically first, then repos alphabetically
    if "/issues/" in u:
        return (0, int(u.rsplit("/", 1)[-1]))
    return (1, u)


def collect(g):
    ucs, reqs = {}, {}
    for uc in g.subjects(RDF.type, LWS_UCR.UseCase):
        ident = text(g, uc, DCTERMS.identifier)
        if ident:
            ucs[uc] = ident
    for rq in g.subjects(RDF.type, LWS_UCR.Requirement):
        ident = text(g, rq, DCTERMS.identifier)
        if ident:
            reqs[rq] = ident
    return ucs, reqs


def motivations(g, ucs, reqs):
    """(uc -> set(req), req -> set(uc)) from motivates union inverse motivatedBy."""
    uc2req = {uc: set() for uc in ucs}
    req2uc = {rq: set() for rq in reqs}
    for uc, rq in g.subject_objects(LWS_UCR.motivates):
        if uc in ucs and rq in reqs:
            uc2req[uc].add(rq)
            req2uc[rq].add(uc)
    for rq, uc in g.subject_objects(LWS_UCR.motivatedBy):
        if uc in ucs and rq in reqs:
            uc2req[uc].add(rq)
            req2uc[rq].add(uc)
    return uc2req, req2uc


def req_link(g, rq, reqs) -> str:
    return f"[{text(g, rq, DCTERMS.title)}](#{anchor(reqs[rq])})"


def uc_link(g, uc, ucs) -> str:
    return f"[{text(g, uc, DCTERMS.title)}](#{anchor(ucs[uc])})"


def status_of(g, node):
    return one(g, node, LWS_UCR.status)


def sort_entities(g, entities, idents):
    """Stable order: status rank, then title."""
    def key(e):
        st = status_of(g, e)
        st_rank = STATUS_ORDER.index(st) if st in STATUS_ORDER else len(STATUS_ORDER)
        return (st_rank, (text(g, e, DCTERMS.title) or idents[e]).lower())
    return sorted(entities, key=key)


def render_scenarios(g, uc, out):
    scens = list(g.objects(uc, LWS_UCR.scenario))
    def skey(s):
        k = one(g, s, LWS_UCR.scenarioKind)
        return (SCENARIO_KIND_ORDER.index(k) if k in SCENARIO_KIND_ORDER else 99, str(s))
    for s in sorted(scens, key=skey):
        kind = SCENARIO_KIND_LABEL.get(one(g, s, LWS_UCR.scenarioKind), "Scenario")
        steps_head = one(g, s, LWS_UCR.steps)
        if steps_head is not None:
            out.append(f"  *{kind}:*")
            for i, step in enumerate(Collection(g, steps_head), 1):
                out.append(f"    {i}. {step}")
        desc = text(g, s, DCTERMS.description)
        if desc:
            out.append(f"  *{kind}:* {desc}")
        out.append("")


def render_use_case(g, uc, ucs, reqs, uc2req, out):
    ident = ucs[uc]
    title = text(g, uc, DCTERMS.title)
    st = status_of(g, uc)
    st_label = label(g, st) if st is not None else "?"
    out.append(f"- **<dfn id=\"{anchor(ident)}\">{title}</dfn>** <span class=\"informative\">"
               f"(`{ident}` — {st_label})</span>")
    out.append("")
    primary = one(g, uc, LWS_UCR.primaryActor)
    actors = set(g.objects(uc, LWS_UCR.actor)) | ({primary} if primary is not None else set())
    goal = text(g, uc, LWS_UCR.goal) or ""
    benefit = text(g, uc, LWS_UCR.benefit) or ""
    actor_name = label(g, primary).lower() if primary is not None else "user"
    article = indefinite_article(actor_name)
    out.append(f"  **As {article}** {actor_name}, **I want** {goal}, **so that** {benefit}.")
    out.append("")
    desc = text(g, uc, DCTERMS.description)
    if desc:
        out.append(f"  *Context:* {desc}")
        out.append("")
    others = sorted(label(g, a).lower() for a in actors if a != primary)
    if others:
        out.append(f"  *Other actors:* {', '.join(others)}.")
        out.append("")
    pres = texts(g, uc, LWS_UCR.precondition)
    if pres:
        out.append("  *Preconditions:* " + " ".join(pres))
        out.append("")
    render_scenarios(g, uc, out)
    posts = texts(g, uc, LWS_UCR.postcondition)
    if posts:
        out.append("  *Postconditions:* " + " ".join(posts))
        out.append("")
    derived = sorted(uc2req.get(uc, ()), key=lambda r: (text(g, r, DCTERMS.title) or "").lower())
    if derived:
        out.append("  *Derived requirements:* " + ", ".join(req_link(g, r, reqs) for r in derived) + ".")
    else:
        out.append("  *Derived requirements:* none yet — this use case is not yet covered by a requirement.")
    out.append("")
    srcs = sorted((str(o) for o in g.objects(uc, LWS_UCR.sourceIssue)), key=source_sort_key)
    if srcs:
        out.append("  *Sources:* " + ", ".join(source_link(s) for s in srcs))
        out.append("")


def gen_user_stories(g, ucs, reqs, uc2req) -> str:
    out = [GENERATED_NOTE]
    out.append("The use cases below are generated from the machine-readable corpus in "
               "[`ucr/`](https://github.com/jeswr/lws-ucs/tree/main/ucr), expressed with the "
               "[`lws-ucr` ontology](https://github.com/jeswr/lws-ucs/blob/main/docs/ontology.md) "
               "and validated by its SHACL shapes: every use case has a stable identifier, a "
               "primary actor from the shared role scheme, and a machine-checked link to the "
               "requirements it motivates. Items marked **Accepted** come from the previously "
               "published document; items marked **Proposed** are new submissions (from open "
               "issue triage or derived from deployed applications) awaiting WG review.")
    out.append("")
    placed = set()
    for group, cats in GROUPS:
        out.append(f"## {group}")
        out.append("")
        for c in cats:
            in_cat = [uc for uc in ucs
                      if uc not in placed and c in set(g.objects(uc, LWS_UCR.category))
                      and CATEGORY_ORDER.index(c) == min(CATEGORY_ORDER.index(cc)
                                                         for cc in g.objects(uc, LWS_UCR.category)
                                                         if cc in CATEGORY_ORDER)]
            if not in_cat:
                continue
            out.append(f"### {label(g, c)}")
            out.append("")
            for uc in sort_entities(g, in_cat, ucs):
                render_use_case(g, uc, ucs, reqs, uc2req, out)
                placed.add(uc)
    leftovers = [uc for uc in ucs if uc not in placed]
    if leftovers:
        out.append("### Uncategorised")
        out.append("")
        for uc in sort_entities(g, leftovers, ucs):
            render_use_case(g, uc, ucs, reqs, uc2req, out)
    return "\n".join(out).rstrip() + "\n"


def render_requirement(g, rq, ucs, reqs, req2uc, out, indent=0):
    pad = "    " * indent
    ident = reqs[rq]
    title = text(g, rq, DCTERMS.title)
    st = status_of(g, rq)
    st_label = label(g, st) if st is not None else None
    prio = one(g, rq, LWS_UCR.priority)
    types = sorted(label(g, t) for t in g.objects(rq, LWS_UCR.requirementType))
    badge = " · ".join(x for x in [", ".join(types) or None,
                                   label(g, prio) if prio is not None else None,
                                   st_label] if x)
    out.append(f"{pad}1. **<dfn id=\"{anchor(ident)}\">{title}</dfn>** "
               f"<span class=\"informative\">(`{ident}` — {badge})</span>")
    out.append("")
    out.append(f"{pad}    {text(g, rq, DCTERMS.description)}")
    out.append("")
    rationale = text(g, rq, LWS_UCR.rationale)
    if rationale:
        out.append(f"{pad}    *Rationale:* {rationale}")
        out.append("")
    motivating = sorted(req2uc.get(rq, ()), key=lambda u: (text(g, u, DCTERMS.title) or "").lower())
    if motivating:
        out.append(f"{pad}    *Motivated by:* " + ", ".join(uc_link(g, u, ucs) for u in motivating) + ".")
        out.append("")
    feats = sorted(label(g, f) for f in g.objects(rq, LWS_UCR.relatedFeature))
    if feats:
        out.append(f"{pad}    *Protocol feature(s):* {', '.join(feats)}.")
        out.append("")
    srcs = sorted((str(o) for o in g.objects(rq, LWS_UCR.sourceIssue)), key=source_sort_key)
    if srcs:
        out.append(f"{pad}    *Sources:* " + ", ".join(source_link(s) for s in srcs))
        out.append("")
    for child in sorted(g.objects(rq, OSLC_RM.decomposedBy),
                        key=lambda r: (text(g, r, DCTERMS.title) or "").lower()):
        if child in reqs:
            render_requirement(g, child, ucs, reqs, req2uc, out, indent + 1)


def gen_requirements(g, ucs, reqs, req2uc) -> str:
    out = [GENERATED_NOTE]
    out.append("The requirements below are generated from the machine-readable corpus in "
               "[`ucr/`](https://github.com/jeswr/lws-ucs/tree/main/ucr). Every requirement "
               "carries an explicit, SHACL-validated `motivatedBy` link to at least one use "
               "case — the *Motivated by* line replaces the previous prose \"Stories:\" "
               "back-references, and a dangling reference is now a validation error. "
               "Modality is normalised to uppercase [[RFC2119]] keywords. "
               "**Priorities (MoSCoW) are provisional editorial assignments** reflecting the "
               "source document's WG-vote ordering and, for proposed items, the submitters' "
               "judgment — they await explicit WG prioritisation. Requirements marked "
               "**Proposed** are new submissions awaiting WG review; unmarked/Accepted items "
               "restate the previously published requirement set.")
    out.append("")
    children = {c for rq in reqs for c in g.objects(rq, OSLC_RM.decomposedBy)}
    top = [rq for rq in reqs if rq not in children]

    def req_key(rq):
        st = status_of(g, rq)
        # Accepted (or unstated == ported) first, then Proposed
        st_rank = 0 if st is None or st == LWS_UCR.Accepted else STATUS_ORDER.index(st)
        prio = one(g, rq, LWS_UCR.priority)
        prio_rank = PRIORITY_ORDER.index(prio) if prio in PRIORITY_ORDER else len(PRIORITY_ORDER)
        return (st_rank, prio_rank, (text(g, rq, DCTERMS.title) or "").lower())

    for rq in sorted(top, key=req_key):
        render_requirement(g, rq, ucs, reqs, req2uc, out)
    return "\n".join(out).rstrip() + "\n"


def gen_matrix(g, ucs, reqs, uc2req) -> str:
    out = [GENERATED_NOTE]
    n_edges = sum(len(v) for v in uc2req.values())
    out.append(f"### Traceability")
    out.append("")
    out.append(f"Generated from the corpus: **{len(ucs)} use cases**, **{len(reqs)} requirements**, "
               f"**{n_edges} motivation links** (each machine-validated: every requirement traces "
               "to at least one use case).")
    out.append("")
    out.append("| Use case | Status | Derived requirements |")
    out.append("| --- | --- | --- |")
    for uc in sorted(ucs, key=lambda u: (text(g, u, DCTERMS.title) or "").lower()):
        st = status_of(g, uc)
        st_label = label(g, st) if st is not None else ""
        derived = sorted(uc2req.get(uc, ()), key=lambda r: (text(g, r, DCTERMS.title) or "").lower())
        cell = ", ".join(req_link(g, r, reqs) for r in derived) if derived else "—"
        out.append(f"| {uc_link(g, uc, ucs)} | {st_label} | {cell} |")
    out.append("")
    uncovered = [uc for uc in ucs if not uc2req.get(uc)]
    if uncovered:
        out.append("The following use cases are not yet covered by any requirement: "
                   + ", ".join(uc_link(g, u, ucs) for u in
                               sorted(uncovered, key=lambda u: (text(g, u, DCTERMS.title) or "").lower()))
                   + ".")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _selftest() -> int:
    """Run the module's doctests (e.g. indefinite_article's article table).

    Returns the failure count; main() treats any failure as fatal so a
    regression in the prose helpers can never silently regenerate wrong text.
    """
    import doctest
    return doctest.testmod(sys.modules[__name__], verbose=False).failed


def main() -> int:
    check = "--check" in sys.argv
    failures = _selftest()
    if failures:
        print(f"SELFTEST FAILED: {failures} doctest failure(s) in generate-spec-md.py",
              file=sys.stderr)
        return 1
    g = load_graph()
    ucs, reqs = collect(g)
    uc2req, req2uc = motivations(g, ucs, reqs)
    outputs = {
        ROOT / "spec" / "user-stories.md": gen_user_stories(g, ucs, reqs, uc2req),
        ROOT / "spec" / "requirements.md": gen_requirements(g, ucs, reqs, req2uc),
        ROOT / "spec" / "requirements-matrix.md": gen_matrix(g, ucs, reqs, uc2req),
    }
    drift = False
    for path, content in outputs.items():
        if check:
            current = path.read_text() if path.exists() else ""
            if current != content:
                print(f"DRIFT: {path.relative_to(ROOT)} does not match the corpus", file=sys.stderr)
                drift = True
            else:
                print(f"ok: {path.relative_to(ROOT)}")
        else:
            path.write_text(content)
            print(f"wrote {path.relative_to(ROOT)} ({len(content.splitlines())} lines)")
    if check and drift:
        return 1
    print(f"{len(ucs)} use cases, {len(reqs)} requirements, "
          f"{sum(len(v) for v in uc2req.values())} motivation edges")
    return 0


if __name__ == "__main__":
    sys.exit(main())
