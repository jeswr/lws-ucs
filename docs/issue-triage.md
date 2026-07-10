<!-- AUTHORED-BY Claude Fable -->

# Open-issue triage — Stage 2 of the UC&R rewrite

**Scope.** As of 2026-07-10 the upstream tracker ([w3c/lws-ucs](https://github.com/w3c/lws-ucs/issues))
has **137 open issues**. Of these, **112 are already cited** by the document and are carried
into the machine-readable corpus as `lws-ucr:sourceIssue` provenance on the corresponding
use case / requirement instance (see `ucr/*.ttl`). The remaining **25 open, uncited issues**
are triaged below: each is assessed **in-scope** (belongs in a UC&R document → written up
with the `lws-ucr` ontology) or **out-of-scope / process** (tracked, but not UC&R content).

Issue #197 ("ensure all use cases on GitHub are captured in the UCR document") is, in
effect, the standing mandate for this exercise.

## Triage table

| Issue | Disposition | Why | Where it landed |
|---|---|---|---|
| [#59 Usage Control](https://github.com/w3c/lws-ucs/issues/59) | **in-scope** | Well-formed UC: constraints on use *after* access; distinct from access control | `UC-usage-control` → `REQ-usage-control` |
| [#66 Purpose-based Access and Usage Control](https://github.com/w3c/lws-ucs/issues/66) | **in-scope** | The purpose dimension of the same usage-control cluster | folded into `UC-usage-control` |
| [#91 Categorization of user stories](https://github.com/w3c/lws-ucs/issues/91) | **in-scope (structural)** | Asks for finer categorization — answered structurally, not by a UC | the SKOS category scheme (`vocab/schemes/categories.ttl`); every UC carries `lws-ucr:category` |
| [#93 Custom validation of mutating requests](https://github.com/w3c/lws-ucs/issues/93) | **in-scope** | Concrete storage capability (shape-validated writes, inbox spam defence) | `UC-mutation-validation` → `REQ-write-validation` |
| [#158 Name actors consistently](https://github.com/w3c/lws-ucs/issues/158) | **in-scope (structural)** | Asks for a consistent actor cast — answered structurally | the SKOS actor-role scheme (`vocab/schemes/roles.ttl`); every UC's `primaryActor`/`actor` draws from it |
| [#159 How to provide feedback on the UC document?](https://github.com/w3c/lws-ucs/issues/159) | **out-of-scope (process)** | WG working-mode/governance question, not a use case or requirement | — (remains a WG process discussion) |
| [#160 "Resource" or "resource"?](https://github.com/w3c/lws-ucs/issues/160) | **out-of-scope (editorial)** | Glossary/terminology consistency, not UC&R content; the transport-neutral definition it proposes belongs in the glossary | — (glossary edit; note `REQ-protocol-decoupling` already carries the transport-neutrality requirement) |
| [#164 Move preserving legacy ACLs](https://github.com/w3c/lws-ucs/issues/164) | **in-scope (already modeled)** | Portability refinement | alternative flow + postcondition of `UC-storage-portability` (Stage 1) |
| [#165 Portability of public resources](https://github.com/w3c/lws-ucs/issues/165) | **in-scope (already modeled)** | Portability refinement | alternative flow + postcondition of `UC-storage-portability` (Stage 1) |
| [#171 Renaming / moving a resource](https://github.com/w3c/lws-ucs/issues/171) | **in-scope** | Distinct from portability (relative-URL tricks don't apply); needs server-side move | `UC-resource-rename-move` → `REQ-rename-move`, `REQ-deletion-signaling` |
| [#192 Write out use case for requirement 33](https://github.com/w3c/lws-ucs/issues/192) | **in-scope (fulfilled)** | Asks for a full UC behind the profile-management requirement | `UC-profile-sharing` elaborated (scenario added); `REQ-profile-management` chain now machine-checked |
| [#195 Pseudonymization + move/delete markers](https://github.com/w3c/lws-ucs/issues/195) | **in-scope (two UCs)** | Two distinct features asked as a question — both real gaps | `UC-pseudonymous-access` → `REQ-pseudonymity`; `UC-link-preservation` → `REQ-deletion-signaling` |
| [#197 Ensure all GitHub UCs are captured](https://github.com/w3c/lws-ucs/issues/197) | **process (meta)** | The mandate for this triage itself | this document + the corpus; every open `[UC]` issue now traced via `lws-ucr:sourceIssue` |
| [#205 Agent notification on access-control change](https://github.com/w3c/lws-ucs/issues/205) | **in-scope (folded)** | Same need as the existing permission-change-notifications story, generalised to agents + attribute issuers | folded into `UC-permission-change-notifications` (sourceIssue + context); `REQ-change-notifications` |
| [#207 User-defined custom API endpoints](https://github.com/w3c/lws-ucs/issues/207) | **in-scope** | A generic extension point absorbing several "add X to the server" asks (virtual resources, extra authz, delegated compute, protocol bridges) | `UC-custom-api-endpoints` → `REQ-extension-endpoints` |
| [#208 Indexed and non-indexed data](https://github.com/w3c/lws-ucs/issues/208) | **in-scope** | Real gap confirmed by local-first apps (CRDT logs must not pollute indexes) | `UC-selective-indexing` → `REQ-indexing-control` |
| [#210 Support for different legal contexts](https://github.com/w3c/lws-ucs/issues/210) | **in-scope (folded)** | Extends the existing legal-grounds story to differing jurisdictions | folded into `UC-legal-grounds-support` (alt scenario); `REQ-legal-basis-enforcement` |
| [#211 ID alias](https://github.com/w3c/lws-ucs/issues/211) | **in-scope** | Alias semantics (multi-identifier entities, individually revocable) | `UC-id-alias` → motivates the multi-identifier clause of `REQ-globally-unique-identifiers` |
| [#212 Discovering who has access](https://github.com/w3c/lws-ucs/issues/212) | **in-scope** | Standing gap; independently confirmed by a real access-management app | `UC-access-overview` → `REQ-authorization-enumeration` |
| [#213 Storage controller vs resource controller](https://github.com/w3c/lws-ucs/issues/213) | **in-scope (clarification)** | A needed clarification of an existing requirement, not a new UC | tracked as `sourceIssue` on `REQ-control-of-storages` + noted in `UC-storage-ownership` |
| [#215 Resource identifier pointing at a different storage](https://github.com/w3c/lws-ucs/issues/215) | **in-scope** | Local statements about foreign identifiers (annotation, ontology caching) | `UC-foreign-identifier-data` → `REQ-external-identifier-access` |
| [#222 Privacy in data discovery](https://github.com/w3c/lws-ucs/issues/222) | **in-scope** | Discovery itself is a disclosure channel; must be a normative constraint | `UC-private-data-discovery` → `REQ-non-leaky-discovery` (also constrains `REQ-app-data-registry`) |
| [#226 Indexing a volunteer profile](https://github.com/w3c/lws-ucs/issues/226) | **in-scope** | End-to-end consented third-party indexing (grant, notify, revoke, remove) | `UC-profile-indexing` → motivates `REQ-consent-based-sharing`, `REQ-change-notifications`, `REQ-usage-control` |
| [#228 Institutional records provability (RecordWeb)](https://github.com/w3c/lws-ucs/issues/228) | **in-scope** | Rich, well-specified UC: sealed snapshots, hash-pinned references, erasure with lineage | `UC-institutional-records` → `REQ-immutable-snapshots`, `REQ-verified-references` (+ existing integrity/deletion reqs) |
| [#229 Import Solid user stories & panel UCRs](https://github.com/w3c/lws-ucs/issues/229) | **process (meta)** | A corpus-import work item (solid/user-stories, authorization-/notifications-panel UCRs), not itself a UC | standing import task; the ontology's `lws-ucr:sourceIssue ⊆ dcterms:source` is built to absorb imported documents |

## Notes

- **Dispositions are editorial proposals** by this fork, recorded so the WG can review them;
  every in-scope write-up is `lws-ucr:Proposed` status in the corpus (never silently
  "Accepted").
- Issues that are open **and already cited** by the document needed no new write-up; their
  citations are preserved as `lws-ucr:sourceIssue` links, which is also how they will be
  found when they are eventually closed or refined.
- The two **structural** answers (#91 categories, #158 actor cast) are load-bearing: the
  SHACL shapes reject a use case whose category or actor is not drawn from the shared
  schemes, so consistency is enforced, not aspirational.
