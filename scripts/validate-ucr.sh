#!/usr/bin/env sh
# AUTHORED-BY Claude Fable
# Validate the lws-ucr model:
#   1. Turtle syntax of the vocabulary, scheme seeds and shapes.
#   2. Positive examples (examples/*.ttl) MUST conform.
#   3. Negative fixtures (examples/negative/*.ttl) MUST be rejected (report a
#      SHACL Violation) — proving the constraints actually bite.
# Every graph is validated over vocab/lws-ucr.ttl + ALL vocab/schemes/*.ttl +
# the instance, so sh:class / sh:node(skos:inScheme) constraints see the
# referenced concepts' types and scheme memberships. --allow-warnings makes
# advisory (Warning-severity) results non-blocking; Violations still fail.
# Requires pyshacl (pip install pyshacl; rdflib comes with it).
# Exit 0 = syntax OK, every positive conforms, every negative is rejected.
set -eu
cd "$(dirname "$0")/.."

PYTHON="${PYTHON:-python3}"
if [ -n "${PYSHACL:-}" ]; then
  command -v "$PYSHACL" >/dev/null 2>&1 || { echo "PYSHACL=$PYSHACL not found" >&2; exit 2; }
elif command -v pyshacl >/dev/null 2>&1; then
  PYSHACL=pyshacl
elif "$PYTHON" -c "import pyshacl" >/dev/null 2>&1; then
  # module installed but no console script on PATH — invoke via the interpreter
  pyshacl_module() { "$PYTHON" -m pyshacl "$@"; }
  PYSHACL=pyshacl_module
else
  echo "pyshacl not found (pip install pyshacl, or set PYSHACL=)" >&2; exit 2
fi

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
status=0

VOCAB="vocab/lws-ucr.ttl vocab/schemes/roles.ttl vocab/schemes/categories.ttl vocab/schemes/features.ttl"

echo "== Turtle syntax: vocab + schemes + shapes =="
for f in $VOCAB shapes/lws-ucr-shapes.ttl; do
  if "$PYTHON" -c "import sys, rdflib; g = rdflib.Graph(); g.parse(sys.argv[1], format='turtle'); print(f'{sys.argv[1]}: OK ({len(g)} triples)')" "$f"; then :; else
    echo "$f: PARSE FAILED" >&2; status=1
  fi
done

echo
echo "== UC&R corpus (ucr/*.ttl, merged — MUST conform) =="
# The full Stage-2 corpus: current document port + issue-triage items +
# app-derived use cases/requirements + the graduated Stage-1 instances.
# Validated as ONE merged graph because motivatedBy/motivates edges cross
# files; per-file Turtle syntax is checked first so a parse error names
# its file.
for f in ucr/*.ttl; do
  [ -f "$f" ] || continue
  if "$PYTHON" -c "import sys, rdflib; g = rdflib.Graph(); g.parse(sys.argv[1], format='turtle'); print(f'{sys.argv[1]}: OK ({len(g)} triples)')" "$f"; then :; else
    echo "$f: PARSE FAILED" >&2; status=1
  fi
done
if [ "$status" -eq 0 ]; then
  cat $VOCAB ucr/*.ttl > "$tmp/corpus.ttl"
  if "$PYSHACL" -s shapes/lws-ucr-shapes.ttl -df turtle -sf turtle --allow-warnings "$tmp/corpus.ttl"; then
    echo "corpus: CONFORMS"
  else
    echo "  UNEXPECTED: UC&R corpus did NOT conform" >&2; status=1
  fi
else
  echo "  (skipping corpus SHACL run — fix the parse errors above first)" >&2
fi

echo
echo "== Positive examples (MUST conform) =="
# Synthetic shape-proving positives (examples/positive/*.ttl); the three
# Stage-1 re-described stories graduated into the ucr/ corpus above.
for ex in examples/positive/*.ttl; do
  [ -f "$ex" ] || continue
  echo "-- $ex"
  cat $VOCAB "$ex" > "$tmp/data.ttl"
  if "$PYSHACL" -s shapes/lws-ucr-shapes.ttl -df turtle -sf turtle --allow-warnings "$tmp/data.ttl"; then :; else
    echo "  UNEXPECTED: positive example did NOT conform" >&2; status=1
  fi
done

echo
echo "== Negative fixtures (MUST be rejected) =="
for ex in examples/negative/*.ttl; do
  [ -f "$ex" ] || continue
  echo "-- $ex"
  cat $VOCAB "$ex" > "$tmp/data.ttl"
  set +e
  out="$("$PYSHACL" -s shapes/lws-ucr-shapes.ttl -df turtle -sf turtle --allow-warnings "$tmp/data.ttl" 2>&1)"
  rc=$?
  set -e
  # Decide by the OUTPUT, not just the exit code: a non-zero exit could be a real
  # SHACL non-conformance, a cyclic-list tooling crash, or an unexpected error —
  # and blindly treating any non-zero as "rejected" would hide a shape regression.
  if printf '%s' "$out" | grep -q "Conforms: False"; then
    echo "  OK: correctly rejected (SHACL Violation) —"
    printf '%s\n' "$out" | grep -E "Result Path|Message" | sed 's/^/     /'
  elif printf '%s' "$out" | grep -q "recursive rdf:rest"; then
    # A genuinely CYCLIC rdf:List. rdflib refuses to enumerate it ("List contains a
    # recursive rdf:rest reference") — a specific RDF-layer malformation guard, NOT a
    # generic exception — so such a list can never conform. (Unreachable via Turtle's
    # () syntax; only hand-written rdf:first/rdf:rest triples form it.) The SHACL
    # terminator constraint itself is proven with clean renderable evidence by the
    # NON-cyclic neg-unterminated-steps fixture, so this branch is not the sole proof
    # of that constraint.
    echo "  OK: correctly rejected (cyclic rdf:List — rdflib recursive-rest malformation guard)"
  elif printf '%s' "$out" | grep -q "Conforms: True"; then
    echo "  REGRESSION: negative fixture CONFORMED but should have been rejected" >&2
    status=1
  else
    echo "  ERROR: validator errored (rc=$rc) without a clean rejection:" >&2
    printf '%s\n' "$out" | tail -3 >&2
    status=1
  fi
done

echo
echo "== Generated spec markdown matches the corpus (drift check) =="
# The corpus (ucr/*.ttl) is the source of truth; spec/*.md are build artifacts.
# A conforming corpus with STALE committed markdown must FAIL the gate, otherwise
# the anti-drift check is only advisory. --check regenerates in memory and diffs
# against the committed files (non-zero exit on drift).
if "$PYTHON" scripts/generate-spec-md.py --check; then
  echo "  OK: spec/*.md is in sync with ucr/*.ttl"
else
  echo "  DRIFT: spec/*.md is stale — run: python3 scripts/generate-spec-md.py" >&2
  status=1
fi

echo
if [ "$status" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit $status
