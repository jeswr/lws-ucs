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

PYSHACL="${PYSHACL:-pyshacl}"
PYTHON="${PYTHON:-python3}"
command -v "$PYSHACL" >/dev/null 2>&1 || { echo "pyshacl not found (pip install pyshacl, or set PYSHACL=)" >&2; exit 2; }

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
echo "== Positive examples (MUST conform) =="
# The three re-described stories (examples/*.ttl) plus synthetic shape-proving
# positives (examples/positive/*.ttl).
for ex in examples/*.ttl examples/positive/*.ttl; do
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
if [ "$status" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit $status
