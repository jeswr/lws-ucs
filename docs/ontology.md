<!-- AUTHORED-BY Claude Fable -->

# The `lws-ucr` ontology — a formal model for LWS use cases & requirements

**Status:** an AI-authored experiment in the `jeswr/lws-ucs` fork. It is **not** a W3C
deliverable and does not speak for the LWS Working Group; it exists so the fork can
re-describe the UC&R document as machine-readable Linked Data and generate the prose from it.

## What it models

Two first-class things and the trace between them:

- **`lws-ucr:UseCase`** — a stakeholder use case: actor role(s), a goal ("I want …"), a
  benefit ("so that …"), context narrative, preconditions, one or more **`lws-ucr:Scenario`**s
  (main / alternative / error flows, prose or ordered steps), postconditions (acceptance
  criteria), a category, a MoSCoW priority, a lifecycle status, and source-issue provenance.
  The current document's "user stories" are simply use cases whose scenario detail has not
  yet been elaborated — the GitHub `[UC]` issue template maps losslessly onto the class.
  The designated "As a …" protagonist is the single **`lws-ucr:primaryActor`** (an
  `owl:FunctionalProperty`, `rdfs:subPropertyOf lws-ucr:actor`); `lws-ucr:actor` lists the
  full cast. The primary actor is an explicit property rather than "the first-listed actor",
  because RDF does not preserve statement order — so with several actors the protagonist would
  otherwise be ambiguous.
- **`lws-ucr:Requirement`** (⊑ `oslc_rm:Requirement`) — a single normative statement
  (`dcterms:description`, RFC 2119-keyworded), typed
  functional / non-functional / security / privacy / interop, MoSCoW-prioritised, with a
  rationale, source issues, optional `lws-ucr:verifiedBy` links to `earl:TestCase`s, and
  inter-requirement dependencies via `dcterms:requires` (plus the whole OSLC RM trace set —
  `oslc_rm:decomposedBy`, `elaboratedBy`, `specifiedBy`, `satisfiedBy` — inherited unchanged).

The load-bearing edge is **`lws-ucr:motivatedBy`** (Requirement → UseCase,
`rdfs:subPropertyOf prov:wasDerivedFrom`, inverse `lws-ucr:motivates`).

## How it fixes the current story↔requirement linkage

Today `spec/requirements.md` back-references stories **by name in prose** ("Stories: Portable
Storage, …") and `spec/requirements-matrix.md` keys rows by section numbers. Names drift,
spellings vary, references dangle, and the matrix covers a fraction of the corpus. In this
model:

- identity is a stable IRI (`dcterms:identifier` slug, never a GitHub issue number — issues
  are provenance via `lws-ucr:sourceIssue ⊑ dcterms:source`, not identity); the shapes require
  use cases and requirements to be IRIs (`sh:nodeKind sh:IRI`), so a blank-node entity is a
  validation error;
- the story↔requirement link is the `motivatedBy` triple, so cross-references and the full
  traceability matrix are **generated**, never hand-typed;
- the SHACL shapes (`shapes/lws-ucr-shapes.ttl`) make a dangling reference a **validation
  error**: every `lws-ucr:Requirement` must have ≥ 1 `motivatedBy` pointing at a real
  `lws-ucr:UseCase`, and controlled values (MoSCoW, status, requirement type, scenario kind)
  must come from the SKOS schemes. Advisory (warning-severity) checks flag missing context,
  missing rationale, and non-RFC 2119 modality.

## Reuse manifest — mint only the use-case layer

The requirement side of this problem is already solved by live, maintained vocabularies; only
the use-case anatomy is minted (no live ontology models it):

| Reused | From | For |
|---|---|---|
| `oslc_rm:Requirement` + trace props (`decomposedBy`, `elaboratedBy`, `specifiedBy`, `satisfiedBy`) | OSLC Requirements Management 2.1 (`http://open-services.net/ns/rm#`) | requirement superclass + decomposition/trace semantics |
| `dcterms:identifier/title/description/source/requires/contributor` | DCMI Terms | stable ID, title, statement, provenance, inter-req deps, contributors |
| `skos:Concept/ConceptScheme/inScheme/prefLabel/definition` | W3C SKOS | every controlled value — no OWL class per enum |
| `prov:wasDerivedFrom` (⊒ `lws-ucr:motivatedBy`), `prov:wasAttributedTo` | W3C PROV-O | the requirement←use-case trace, visible to generic PROV tooling |
| `earl:TestRequirement`, `earl:TestCase`, `earl:Assertion` | W3C EARL 1.0 (`http://www.w3.org/ns/earl#`) | dual-typing testable requirements; `lws-ucr:verifiedBy` targets `earl:TestCase`, so a test suite can emit EARL implementation reports with zero new terms |
| `rdfs:seeAlso`, `vann:preferredNamespacePrefix/Uri` | RDFS / VANN | informative refs, vocab housekeeping |

Considered and not reused: SWORE (right shape, dead namespace — its `conflictsWith` idea is
re-minted as `lws-ucr:conflictsWith`); ReqIF/SysML (not web vocabularies; OSLC RM carries
their trace semantics); `schema:HowToStep` (cooking-instruction semantics for scenario steps);
ODRL (subject matter of LWS use cases, not the meta-model).

## Namespace & persistent-ID plan

- Core vocabulary: **`https://jeswr.org/ns/lws-ucr#`** (prefix `lws-ucr:`) — a **hash**
  namespace: ~4 classes + ~18 properties + the closed enum schemes is one document, one fetch.
- Open-ended controlled vocabularies get **slash sub-paths** so they can grow without
  churning the core document: `…/lws-ucr/roles#` (actor roles, `vocab/schemes/roles.ttl`),
  `…/lws-ucr/categories#` (`vocab/schemes/categories.ttl`), `…/lws-ucr/features#`
  (`vocab/schemes/features.ttl`); SHACL shapes sit at `…/lws-ucr/shapes#`.
- Per the suite persistent-ID policy, the IRIs are served from **`jeswr.org`** via the
  `jeswr/portfolio` redirect layer (303 conneg to this repo's Turtle + an HTML view); the
  registry row in `portfolio/config/persistent-ids.ts` is a follow-on work item. Nothing is
  minted in `w3.org` or `w3id.org` space; if the WG ever adopts the model it would re-mint
  under `w3.org/ns/` with `owl:equivalentClass/Property` bridges.
- Source of truth for the vocabulary is `vocab/lws-ucr.ttl` in this repo.

## Files

- `vocab/lws-ucr.ttl` — the ontology (classes, properties, closed enum schemes).
- `vocab/schemes/{roles,categories,features}.ttl` — seed concepts for the open schemes
  (roles seeded from the glossary cast of w3c/lws-ucs#158; categories from the ten
  sub-category headings of `spec/user-stories.md`, per w3c/lws-ucs#91; features to be
  aligned with a protocol capability registry).
- `shapes/lws-ucr-shapes.ttl` — SHACL Core shapes for well-formed instances.
- `examples/*.ttl` — three stories from the current document re-described as instances
  (Large File Uploads #18, Administrative Assistant #10, Portable Storage #30 + the
  #164/#165 refinements), each with its derived requirement(s).
- `examples/positive/*.ttl` — synthetic shape-proving positives that MUST conform (e.g. a
  use case that names only its `primaryActor`, since `primaryActor rdfs:subPropertyOf actor`
  makes it also an actor — so a separate `actor` value is not required).
- `examples/negative/*.ttl` — eleven single-defect fixtures the shapes MUST reject, each valid
  *except* the one constraint it targets: empty / bare-literal / improperly-terminated
  (non-cyclic) / cyclic step list; a wrong-scheme actor; a wrong-scheme feature; a dangling
  requirement; a bad identifier; a bad-enum status; a missing `primaryActor`; and a blank-node
  entity. The gate asserts each is reported non-conforming, so a shape regression that let a
  fixture conform is caught. (A cyclic `rdf:List` is malformed RDF that rdflib refuses to
  enumerate, so it can never conform; the `nil`-terminator SHACL constraint itself is proven
  with clean renderable evidence by the non-cyclic improperly-terminated fixture.)
- `scripts/validate-ucr.sh` — parses the vocabulary and runs the positive/negative SHACL gate
  with [pySHACL](https://github.com/RDFLib/pySHACL) (`pip install pyshacl`).

## Validating

```sh
pip install pyshacl
sh scripts/validate-ucr.sh
```

Each example is validated over a data graph merged with the vocabulary and scheme seeds (so
`sh:class`/`sh:node` constraints see the referenced concepts' types and scheme memberships).
Violation-severity results fail the gate; advisory warnings are reported but non-blocking
(the script passes `--allow-warnings`). The positive examples conform (with no warnings) and
every negative fixture is reported non-conforming.
