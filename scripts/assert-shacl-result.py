#!/usr/bin/env python3
"""Assert that a pySHACL report contains a fixture's intended violation."""

import sys
from pathlib import Path
from typing import Optional

from rdflib import Graph, Namespace, RDF, URIRef


SH = Namespace("http://www.w3.org/ns/shacl#")
PREFIXES = {
    "sh": "http://www.w3.org/ns/shacl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dcterms": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "lws-ucr": "https://jeswr.org/ns/lws-ucr#",
    "ucrsh": "https://jeswr.org/ns/lws-ucr/shapes#",
}
METADATA_PREFIX = "# EXPECTED-VIOLATION: "


def expand_curie(value: str) -> Optional[URIRef]:
    if value == "-":
        return None
    prefix, separator, local = value.partition(":")
    if not separator or prefix not in PREFIXES or not local:
        raise ValueError(f"unsupported expected term {value!r}")
    return URIRef(PREFIXES[prefix] + local)


def expected_fields(fixture: Path) -> dict[str, str]:
    declarations = [
        line.removeprefix(METADATA_PREFIX).strip()
        for line in fixture.read_text(encoding="utf-8").splitlines()
        if line.startswith(METADATA_PREFIX)
    ]
    if len(declarations) != 1:
        raise ValueError(
            f"{fixture}: expected exactly one {METADATA_PREFIX.strip()} declaration"
        )

    fields: dict[str, str] = {}
    for item in declarations[0].split():
        key, separator, value = item.partition("=")
        if not separator or key not in {"constraint", "path", "sourceShape"}:
            raise ValueError(f"{fixture}: invalid expected-violation field {item!r}")
        fields[key] = value

    if "constraint" not in fields or not ({"path", "sourceShape"} & fields.keys()):
        raise ValueError(
            f"{fixture}: expectation needs constraint and path and/or sourceShape"
        )
    return fields


def describe(report: Graph, result) -> str:
    component = report.value(result, SH.sourceConstraintComponent)
    path = report.value(result, SH.resultPath)
    source_shape = report.value(result, SH.sourceShape)
    return (
        f"constraint={component.n3(report.namespace_manager)} "
        f"path={path.n3(report.namespace_manager) if path is not None else '-'} "
        f"sourceShape={source_shape.n3(report.namespace_manager)}"
    )


def main() -> int:
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} REPORT.ttl FIXTURE.ttl", file=sys.stderr)
        return 2

    report_path = Path(sys.argv[1])
    fixture = Path(sys.argv[2])
    try:
        expected = expected_fields(fixture)
        expanded = {key: expand_curie(value) for key, value in expected.items()}
        report = Graph().parse(report_path, format="turtle")
    except (OSError, ValueError, SyntaxError) as error:
        print(f"  ERROR: {error}", file=sys.stderr)
        return 1

    report_node = next(report.subjects(RDF.type, SH.ValidationReport), None)
    conforms = report.value(report_node, SH.conforms) if report_node is not None else None
    if conforms is None or bool(conforms.toPython()):
        print("  REGRESSION: validation report does not declare sh:conforms false", file=sys.stderr)
        return 1

    violations = [
        result
        for result in report.subjects(RDF.type, SH.ValidationResult)
        if report.value(result, SH.resultSeverity) == SH.Violation
    ]
    for result in violations:
        if report.value(result, SH.sourceConstraintComponent) != expanded["constraint"]:
            continue
        if "path" in expanded and report.value(result, SH.resultPath) != expanded["path"]:
            continue
        if "sourceShape" in expanded and report.value(result, SH.sourceShape) != expanded["sourceShape"]:
            continue
        print(f"  OK: intended violation observed ({describe(report, result)})")
        return 0

    print(
        "  REGRESSION: report is non-conforming, but the intended violation was absent",
        file=sys.stderr,
    )
    print(f"     expected: {' '.join(f'{key}={value}' for key, value in expected.items())}", file=sys.stderr)
    for result in violations:
        print(f"     actual:   {describe(report, result)}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
