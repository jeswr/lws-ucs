<!-- GENERATED from ucr/*.ttl by scripts/generate-spec-md.py — DO NOT EDIT BY HAND.
     Edit the Turtle corpus and regenerate (python3 scripts/generate-spec-md.py). -->

The requirements below are generated from the machine-readable corpus in [`ucr/`](https://github.com/jeswr/lws-ucs/tree/main/ucr). Every requirement carries an explicit, SHACL-validated `motivatedBy` link to at least one use case — the *Motivated by* line replaces the previous prose "Stories:" back-references, and a dangling reference is now a validation error. Modality is normalised to uppercase [[RFC2119]] keywords. **Priorities (MoSCoW) are provisional editorial assignments** reflecting the source document's WG-vote ordering and, for proposed items, the submitters' judgment — they await explicit WG prioritisation. Requirements marked **Proposed** are new submissions awaiting WG review; unmarked/Accepted items restate the previously published requirement set.

1. **<dfn id="req-access-request-handling">Access Request Handling</dfn>** <span class="informative">(`REQ-access-request-handling` — Functional · Must have · Accepted)</span>

    The protocol MUST enable an entity to easily request access to a resource they are currently not authorized to access, and allow the resource owner (or controller) to easily review and grant or deny such requests. There MUST be a standard way for a requester to signal a desire for access, and for the owner to be notified and respond. This ensures that data owners can share particular data upon request without preemptively granting broad access.

    *Rationale:* Request-then-grant is how sharing actually starts; without a standard flow every app invents an incompatible one.

    *Motivated by:* [Business Data Access](#uc-business-data-access), [Health Record Access](#uc-health-record-access).

    *Protocol feature(s):* Authorization.

    *Sources:* [#11](https://github.com/w3c/lws-ucs/issues/11), [#28](https://github.com/w3c/lws-ucs/issues/28), [#78](https://github.com/w3c/lws-ucs/issues/78), [#79](https://github.com/w3c/lws-ucs/issues/79), [#92](https://github.com/w3c/lws-ucs/issues/92)

1. **<dfn id="req-resource-crud">Adding, Updating, Deleting Resources in Storage</dfn>** <span class="informative">(`REQ-resource-crud` — Functional · Must have · Accepted)</span>

    The protocol MUST allow resources to be added, updated and/or deleted within a storage by authorized entities. In general the protocol MUST allow any type of resource to be stored in a storage; storage providers MAY impose certain limitations, such as of type or size.

    *Rationale:* The foundational read/write surface every other capability builds on.

    *Motivated by:* [Generic Storage](#uc-generic-storage).

    *Protocol feature(s):* Resource management.

    *Sources:* [#117](https://github.com/w3c/lws-ucs/issues/117), [#124](https://github.com/w3c/lws-ucs/issues/124)

1. **<dfn id="req-authentication-mechanisms">Authentication Mechanisms</dfn>** <span class="informative">(`REQ-authentication-mechanisms` — Functional, Security · Must have · Accepted)</span>

    The protocol MUST support centralized, federated, and/or self-sovereign types of authentication mechanism.

    *Rationale:* Loose coupling of identity from storage is a charter goal; no single authentication topology can be mandated.

    *Motivated by:* [Authentication Mechanism(s)](#uc-authentication-mechanisms), [Identity & Credentials Management](#uc-identity-credentials-management).

    *Protocol feature(s):* Authentication.

    *Sources:* [#25](https://github.com/w3c/lws-ucs/issues/25), [#39](https://github.com/w3c/lws-ucs/issues/39), [#49](https://github.com/w3c/lws-ucs/issues/49), [#90](https://github.com/w3c/lws-ucs/issues/90), [#115](https://github.com/w3c/lws-ucs/issues/115), [#128](https://github.com/w3c/lws-ucs/issues/128)

1. **<dfn id="req-consent-based-sharing">Consent-Based Data Sharing</dfn>** <span class="informative">(`REQ-consent-based-sharing` — Privacy · Must have · Accepted)</span>

    The protocol MUST provide a means to record and honor user consent for data sharing, including whom they are sharing with, what they are sharing, the purpose of the sharing, and its duration. There MUST be a verifiable, auditable record of user consent (e.g., receipts or tokens) that is revocable, ensuring access removal upon withdrawal of consent.

    *Rationale:* Regulated data sharing (GDPR consent basis) requires demonstrable, revocable consent — not just an ACL entry.

    *Motivated by:* [Consent-Based Sharing](#uc-consent-based-sharing), [Indexing a Volunteer Profile](#uc-profile-indexing).

    *Protocol feature(s):* Audit and accountability, Authorization.

    *Sources:* [#81](https://github.com/w3c/lws-ucs/issues/81), [#141](https://github.com/w3c/lws-ucs/issues/141)

1. **<dfn id="req-control-of-storages">Control of Storages</dfn>** <span class="informative">(`REQ-control-of-storages` — Functional · Must have · Accepted)</span>

    An entity MUST be able to control one or more storages across one or more storage providers. A storage MUST have exactly one controller; this controller MAY be an abstract entity such as a group, rather than necessarily an individual person or agent.

    *Rationale:* Unambiguous control is the root of the authorization model; the storage-controller vs resource-controller relationship remains under WG clarification (issue #213).

    *Motivated by:* [Storage Ownership](#uc-storage-ownership).

    *Protocol feature(s):* Authorization.

    *Sources:* [#130](https://github.com/w3c/lws-ucs/issues/130), [#213](https://github.com/w3c/lws-ucs/issues/213)

1. **<dfn id="req-data-sharing">Data Sharing</dfn>** <span class="informative">(`REQ-data-sharing` — Functional · Must have · Accepted)</span>

    The protocol MUST allow an entity to grant access to a resource it controls to another entity — allowing that entity to perform some operations (read, modify, remove, ...) on the resource. An access grant MAY be temporary (have an expiration time) or open-ended. The granting entity MUST be able to modify such a grant at a later time, by changing the expiration or revoking the grant altogether.

    *Rationale:* Fine-grained, revocable sharing is the core promise of user-controlled storage; four independent stories converge on it.

    *Motivated by:* [Group Sharing](#uc-group-sharing), [Health Record Access](#uc-health-record-access), [Profile Sharing](#uc-profile-sharing), [Sharing Access](#uc-sharing-access).

    *Protocol feature(s):* Authorization.

    *Sources:* [#27](https://github.com/w3c/lws-ucs/issues/27), [#118](https://github.com/w3c/lws-ucs/issues/118)

1. **<dfn id="req-delegation-of-access-rights">Delegation of Access Rights</dfn>** <span class="informative">(`REQ-delegation-of-access-rights` — Functional · Must have · Accepted)</span>

    The protocol MUST allow an entity to delegate a proper subset of its access rights to another entity, such that the delegate's actions are authorized by the delegation, remain attributable to the delegate, and the delegation can be revoked independently of any other grant.

    *Rationale:* Delegation recurs across the corpus (assistant #10, health-record AI #11, autonomous-group re-delegation #104, generic delegation #118); a subset-scoped, independently revocable, attributable delegation primitive is the common core.

    *Motivated by:* [Administrative Assistant](#uc-administrative-assistant), [Health Record Access](#uc-health-record-access).

    *Protocol feature(s):* Authorization.

    *Sources:* [#10](https://github.com/w3c/lws-ucs/issues/10), [#104](https://github.com/w3c/lws-ucs/issues/104), [#118](https://github.com/w3c/lws-ucs/issues/118)

1. **<dfn id="req-globally-unique-identifiers">Globally Unique Identifiers</dfn>** <span class="informative">(`REQ-globally-unique-identifiers` — Functional, Interoperability · Must have · Accepted)</span>

    Resources, including entities and storages, MUST be uniquely identifiable globally. No two distinct resources SHALL share the same identifier (though a 'collective' resource with one identifier may comprise several resources, each with its own identifier, and actions on the collective resource can affect the resources comprising it). Further, a resource MAY be identifiable via multiple, distinct identifiers.

    *Rationale:* Global identity underpins cross-storage reference, access control and portability; the multi-identifier clause also carries the ID-alias need of issue #211.

    *Motivated by:* [Globally Unique Identity](#uc-globally-unique-identifiers), [ID Alias](#uc-id-alias).

    *Protocol feature(s):* Identity.

    *Sources:* [#108](https://github.com/w3c/lws-ucs/issues/108), [#136](https://github.com/w3c/lws-ucs/issues/136)

1. **<dfn id="req-group-access-control">Group-Based Access Control</dfn>** <span class="informative">(`REQ-group-access-control` — Functional · Must have · Accepted)</span>

    The protocol MUST allow controllers to define and manage groups of entities, apply access control rules at the group level, and dynamically propagate membership changes so that permissions update automatically as the group evolves. The protocol SHOULD also allow group hierarchies (nested groups), e.g. Solid-admin defined as a subset of Solid-contributors, so permissions given to Solid-contributors also apply to Solid-admin.

    *Rationale:* Per-individual grants do not scale to changing collaborations; groups are the unit real organisations manage.

    *Motivated by:* [Group Sharing](#uc-group-sharing).

    *Protocol feature(s):* Authorization.

    *Sources:* [#38](https://github.com/w3c/lws-ucs/issues/38), [#102](https://github.com/w3c/lws-ucs/issues/102)

1. **<dfn id="req-offline-sync">Offline Access and Synchronization</dfn>** <span class="informative">(`REQ-offline-sync` — Functional · Must have · Accepted)</span>

    The protocol MUST allow entities to access and modify data even when disconnected from the network, with local changes synchronized to the online storage once connectivity is restored. This includes providing strong guarantees against data corruption and robust conflict resolution to ensure data consistency after offline edits.

    *Rationale:* Unreliable connectivity is the norm, not the exception; synchronization semantics must be part of the protocol contract, not app folklore.

    *Motivated by:* [Deletion Visibility for Replicas](#uc-replica-deletion-sync), [Offline Data Access](#uc-offline-data-access), [Offline-First Instant Load](#uc-offline-first-instant-load), [Storage Listening](#uc-storage-listening).

    *Protocol feature(s):* Offline and synchronization.

1. **<dfn id="req-performance-scalability">Performance and Scalability</dfn>** <span class="informative">(`REQ-performance-scalability` — Non-functional · Must have · Accepted)</span>

    The protocol and its implementations MUST be designed for high performance at scale. Access control checks and data operations SHOULD incur minimal overhead, and the design SHOULD allow batching, caching, and distributed/clustered deployments to meet typical web performance needs.

    *Rationale:* Per-request access-control evaluation is the hot path; a design that cannot be cached or distributed fails at web scale.

    *Motivated by:* [Durable Save on Exit](#uc-durable-exit-save), [Performant Access Control](#uc-performant-access-control).

    *Protocol feature(s):* Operations.

    *Sources:* [#72](https://github.com/w3c/lws-ucs/issues/72)

1. **<dfn id="req-self-descriptive-apis">Self-Descriptive and Discoverable APIs</dfn>** <span class="informative">(`REQ-self-descriptive-apis` — Functional, Interoperability · Must have · Accepted)</span>

    The protocol MUST include means by which services can discover a storage's available capabilities and uniformly navigate its data and access control interfaces, so that services can store, read, update, and delete their data within user-managed storages and users retain ownership of app-generated content. This might be achieved via hypermedia controls or standard descriptors in responses (e.g., JSON-LD links indicating available actions or endpoints). Servers SHOULD provide a discoverable description of their supported protocol versions, extensions, and features.

    *Rationale:* Apps meeting an unknown storage must be able to adapt without out-of-band knowledge; discovery is what decouples app from provider.

    *Motivated by:* ['Bring Your Own Data' Apps](#uc-byod-apps), [Hypermedia Authoring](#uc-hypermedia-authoring), [Storage Description and Discovery](#uc-storage-description-discovery).

    *Protocol feature(s):* Discovery.

    *Sources:* [#12](https://github.com/w3c/lws-ucs/issues/12), [#21](https://github.com/w3c/lws-ucs/issues/21), [#70](https://github.com/w3c/lws-ucs/issues/70), [#120](https://github.com/w3c/lws-ucs/issues/120)

1. **<dfn id="req-serialization-format">Serialization Format</dfn>** <span class="informative">(`REQ-serialization-format` — Interoperability · Must have · Accepted)</span>

    The protocol MUST make it possible for data in a storage to be serialized in a known format.

    *Rationale:* Known serializations are the precondition of any cross-application interoperability.

    *Motivated by:* [Cross-Application Data Interoperability](#uc-cross-app-interop), [Data Integration](#uc-data-integration), [Migrating an Existing App onto User Storage](#uc-legacy-app-migration), [Personal Information Management](#uc-personal-information-management).

    *Protocol feature(s):* Resource management.

1. **<dfn id="req-storage-portability">Storage Portability</dfn>** <span class="informative">(`REQ-storage-portability` — Interoperability · Must have · Accepted)</span>

    The protocol MUST enable an entity to move an entire storage between providers such that resource identity, data integrity, standing access grants, and public availability of published resources are preserved, and the former provider is released of responsibility.

    *Rationale:* Loose provider coupling is the doc's own framing of LWS's purpose; #164/#165 show naive export/import (bytes only) fails the actual sovereignty goal.

    *Motivated by:* [Portable Storage](#uc-storage-portability).

    *Protocol feature(s):* Storage portability.

    *Sources:* [#30](https://github.com/w3c/lws-ucs/issues/30), [#140](https://github.com/w3c/lws-ucs/issues/140)

1. **<dfn id="req-change-notifications">Subscribing to Resource Changes (Notifications)</dfn>** <span class="informative">(`REQ-change-notifications` — Functional · Must have · Accepted)</span>

    The protocol MUST provide a mechanism to notify relevant entities of significant events, such as changes to resources or updates to access permissions. For example, if access rights on a resource change or new data is made available, the affected parties can be alerted in a timely manner. Notification delivery MAY be real-time (e.g., push/SSE) or via queued channels (e.g., email or inbox), respecting user preferences and privacy.

    *Rationale:* Collaboration and permission awareness both need change propagation; polling does not scale and leaks intent.

    *Motivated by:* [Application Notifications](#uc-application-notifications), [Federated Task Dashboard](#uc-federated-task-dashboard), [Indexing a Volunteer Profile](#uc-profile-indexing), [Notifications for Permission Changes](#uc-permission-change-notifications), [Offline-First Instant Load](#uc-offline-first-instant-load), [Real-Time Notifications](#uc-real-time-notifications).

    *Protocol feature(s):* Notifications.

    *Sources:* [#32](https://github.com/w3c/lws-ucs/issues/32), [#100](https://github.com/w3c/lws-ucs/issues/100), [#101](https://github.com/w3c/lws-ucs/issues/101), [#205](https://github.com/w3c/lws-ucs/issues/205)

1. **<dfn id="req-trusted-identity-providers">Trusted Identity Providers</dfn>** <span class="informative">(`REQ-trusted-identity-providers` — Security · Must have · Accepted)</span>

    The protocol MUST enable storage providers to establish trust relationships with identity providers of their choosing, rather than blindly accepting any identity source (though such blind acceptance SHOULD also be a configurable option). Trust is non-transitive: a storage does not inherit trust relationships; it only accepts credentials from identity providers it is configured to trust (which might be or include a wildcard, e.g., for website content intended for general consumption).

    *Rationale:* An issuer-agnostic-but-configurable trust list is what keeps identity swappable without making every storage accept every issuer.

    *Motivated by:* [Trust Mechanism for Storage Providers](#uc-storage-provider-trust).

    *Protocol feature(s):* Authentication.

    *Sources:* [#129](https://github.com/w3c/lws-ucs/issues/129)

1. **<dfn id="req-auditable-trail">Auditable Trail</dfn>** <span class="informative">(`REQ-auditable-trail` — Security · Should have · Accepted)</span>

    The protocol MUST enable a resource controller to obtain an auditable record of accesses to their resources, including, for delegated access, the identity of the acting delegate and the grant under which they acted.

    *Rationale:* Accountability is the counterpart of delegation: without an attributable trail, subset delegation degenerates to credential sharing.

    *Motivated by:* [Administrative Assistant](#uc-administrative-assistant), [AI Agent Access to Storage](#uc-ai-agent-access), [Digital Goods Delivery](#uc-digital-goods-delivery), [Health Record Access](#uc-health-record-access), [Legal Reporting](#uc-legal-reporting).

    *Protocol feature(s):* Audit and accountability.

    *Sources:* [#10](https://github.com/w3c/lws-ucs/issues/10), [#84](https://github.com/w3c/lws-ucs/issues/84), [#85](https://github.com/w3c/lws-ucs/issues/85)

1. **<dfn id="req-contextual-access-control">Contextual Access Control</dfn>** <span class="informative">(`REQ-contextual-access-control` — Functional, Security · Should have · Accepted)</span>

    The access control mechanisms MUST support context-aware policies. An entity SHOULD be able to impose additional conditions on resource access based on contexts such as time windows, location, and group membership status, among others. For instance, a policy could allow access only during certain hours, or only if the requesting party is within a specific role or group at the time.

    *Rationale:* Static grants cannot express real-world conditions (working hours, presence, jurisdiction).

    *Motivated by:* [Context-Aware Access Policies](#uc-context-aware-access-policies).

    *Protocol feature(s):* Authorization.

    *Sources:* [#17](https://github.com/w3c/lws-ucs/issues/17), [#65](https://github.com/w3c/lws-ucs/issues/65), [#179](https://github.com/w3c/lws-ucs/issues/179)

1. **<dfn id="req-data-integrity-verification">Data Integrity Verification</dfn>** <span class="informative">(`REQ-data-integrity-verification` — Security · Should have · Accepted)</span>

    The protocol MUST incorporate mechanisms to ensure and verify the integrity of stored data. Authorized entities SHOULD be able to detect whether data has been tampered with or corrupted (at rest or in transit). For example, the system may use cryptographic hashes, signatures, and/or checksums such that clients can confirm that a resource retrieved from storage is exactly as originally stored by the owner.

    *Rationale:* Verifiable integrity is the precondition of legal-grade records and of portability verification.

    *Motivated by:* [Institutional Records Provability](#uc-institutional-records), [Legal Reporting](#uc-legal-reporting).

    *Protocol feature(s):* Encryption.

1. **<dfn id="req-delegation-of-control">Delegation of Control</dfn>** <span class="informative">(`REQ-delegation-of-control` — Functional · Should have · Accepted)</span>

    The protocol MUST allow an entity to delegate control of a storage to another entity. Such delegation MAY be temporary (have an expiration date and time) or permanent. An entity MUST be able to modify its delegations at a later time, such as by changing expiration or revoking the delegation altogether.

    *Rationale:* Whole-storage administration must be transferable without credential sharing (assistants, organisational change).

    *Motivated by:* [Delegating Control of a Storage](#uc-delegation-of-control).

    *Protocol feature(s):* Authorization.

1. **<dfn id="req-e2e-encryption">End-to-End Encryption</dfn>** <span class="informative">(`REQ-e2e-encryption` — Privacy, Security · Should have · Accepted)</span>

    The protocol MUST enable end-to-end encryption of data such that data stored or transmitted is unreadable to anyone except the authorized parties. Even storage providers or network intermediaries cannot decrypt the content (only the data owner and intended recipients can). End-to-end encryption SHOULD be achievable for data at rest and in transit, using standard algorithms.

    *Rationale:* Provider-blind confidentiality is the strongest trust reduction the protocol can offer; it must be designed for, not bolted on.

    *Motivated by:* ['End to End' Encryption](#uc-e2e-encryption).

    *Protocol feature(s):* Encryption.

    *Sources:* [#4](https://github.com/w3c/lws-ucs/issues/4), [#44](https://github.com/w3c/lws-ucs/issues/44)

1. **<dfn id="req-inbox">Inbox (Notifications)</dfn>** <span class="informative">(`REQ-inbox` — Functional · Should have · Accepted)</span>

    The protocol MUST provide a mechanism for users (or their agents/applications) to exchange messages or data directly via their storages in a standardized way, enabling built-in collaboration without relying on external messaging services. For example, a user can send a message, notification, or invite to another user's storage (with appropriate authorization), and the receiving user's client can retrieve or be alerted to this message.

    *Rationale:* Storage-to-storage message delivery (an inbox) is the collaboration primitive invitations, scheduling and access requests all build on.

    *Motivated by:* [Crawling and Indexing Public Storage Data](#uc-public-index-crawl), [Meeting Scheduling](#uc-meeting-scheduling), [Universal Communication](#uc-universal-communication).

    *Protocol feature(s):* Notifications.

    *Sources:* [#22](https://github.com/w3c/lws-ucs/issues/22), [#99](https://github.com/w3c/lws-ucs/issues/99)

1. **<dfn id="req-legal-basis-enforcement">Legal Basis Enforcement</dfn>** <span class="informative">(`REQ-legal-basis-enforcement` — Privacy · Should have · Accepted)</span>

    The protocol MUST support associating access control decisions with legal bases or policies. For example, implementers SHOULD be able to tag data access rules with specific legal grounds (such as 'Consent – GDPR Article 6(1)(a)' or 'Contract – GDPR Article 6(1)(b)'), and record these as metadata alongside audit trails.

    *Rationale:* Regulated deployments must show WHY access was allowed, not just that it was; differing legal contexts (issue #210) make the basis explicit.

    *Motivated by:* [Legal Grounds Support](#uc-legal-grounds-support).

    *Protocol feature(s):* Audit and accountability.

    *Sources:* [#77](https://github.com/w3c/lws-ucs/issues/77), [#80](https://github.com/w3c/lws-ucs/issues/80), [#210](https://github.com/w3c/lws-ucs/issues/210)

1. **<dfn id="req-protocol-decoupling">Loose Coupling of Underlying Protocols</dfn>** <span class="informative">(`REQ-protocol-decoupling` — Interoperability · Should have · Accepted)</span>

    The core data access and identity interactions MUST be defined abstractly, decoupled from any single transport or encoding. While HTTP(S) is expected, the protocol's semantics MUST be mappable to alternative or future transports (e.g., gRPC, GraphQL over WebSocket, local IPC) without changing its fundamental model.

    *Rationale:* Local-first and embedded scenarios need the semantics without the HTTP stack; abstract definition keeps the door open.

    *Motivated by:* [API Protocol Decoupling](#uc-api-protocol-decoupling).

    *Protocol feature(s):* Extensibility.

    *Sources:* [#24](https://github.com/w3c/lws-ucs/issues/24)

1. **<dfn id="req-personal-data-projection">Personal Data Projection</dfn>** <span class="informative">(`REQ-personal-data-projection` — Interoperability · Should have · Accepted)</span>

    The protocol MUST provide a mechanism to support automatic transformation (projection) of personal data into formats consumable by non-LWS applications (e.g., JSON, vCard), without duplicating underlying resources, to prevent data silos and provide compatibility and interoperability with existing web standards. This may also apply to converting from one LWS data schema or structure to another, for interoperability across LWS applications.

    *Rationale:* Compatibility with the existing app ecosystem cannot require every consumer to speak RDF; projection bridges without duplication.

    *Motivated by:* [Personal Information Management](#uc-personal-information-management).

    *Protocol feature(s):* Extensibility.

    *Sources:* [#2](https://github.com/w3c/lws-ucs/issues/2)

1. **<dfn id="req-profile-management">Profile Management</dfn>** <span class="informative">(`REQ-profile-management` — Functional, Privacy · Should have · Accepted)</span>

    The protocol MUST support entities having multiple distinct profiles (e.g., 'work' vs. 'personal'), each with its own identifiers, metadata namespaces and access-control rules, so that data can be selectively shared under different personas.

    *Rationale:* Contextual identity separation is a privacy requirement, not a convenience: linking personas leaks by default.

    *Motivated by:* [Profile Sharing](#uc-profile-sharing).

    *Protocol feature(s):* Identity.

    *Sources:* [#192](https://github.com/w3c/lws-ucs/issues/192)

1. **<dfn id="req-resource-versioning">Resource Versioning</dfn>** <span class="informative">(`REQ-resource-versioning` — Functional · Should have · Accepted)</span>

    The protocol MUST support maintaining and retrieving previous versions of resources. Authorized entities SHOULD be able to recover or inspect earlier versions of data (including metadata and access control states) to enable modification audits and change reversion, including recovery from accidental deletions.

    *Rationale:* Durability and traceability over time: version recovery is named in the foundational storage story itself.

    *Motivated by:* [Generic Storage](#uc-generic-storage).

    *Protocol feature(s):* Resource management.

1. **<dfn id="req-resumable-uploads">Resumable Large Data Transfers</dfn>** <span class="informative">(`REQ-resumable-uploads` — Functional · Should have · Accepted)</span>

    The protocol MUST provide a mechanism by which a client can resume an interrupted resource upload without retransmitting bytes the server has already durably received, and a partially transferred representation MUST NOT be observable at the target URI.

    *Rationale:* Large-media use cases fail on consumer connections without resumability; aligning with IETF Resumable Uploads for HTTP avoids inventing a parallel mechanism (the current doc's one localBiblio entry).

    *Motivated by:* [Large File Uploads](#uc-large-file-uploads).

    *Protocol feature(s):* Resource management.

    *Sources:* [#18](https://github.com/w3c/lws-ucs/issues/18)

1. **<dfn id="req-search-and-query">Search and Query</dfn>** <span class="informative">(`REQ-search-and-query` — Functional · Should have · Accepted)</span>

    The protocol MUST provide query capabilities over data in storages, respecting access control, so that relevant resources can be found in potentially large storages. This requirement decomposes into pod-level, metadata, resource-level, cross-storage, result-set-management and federated query requirements.

    *Rationale:* Search over large personal datasets is unusable client-side-only; every query must respect ACLs or it becomes an oracle.

    *Motivated by:* [Pagination & Filtering](#uc-pagination-filtering), [Search Functionality](#uc-search-functionality), [SPARQL Queries](#uc-sparql-queries).

    *Protocol feature(s):* Query and search.

    *Sources:* [#45](https://github.com/w3c/lws-ucs/issues/45), [#152](https://github.com/w3c/lws-ucs/issues/152)

    1. **<dfn id="req-federated-query-joins">Federated Query Joins</dfn>** <span class="informative">(`REQ-federated-query-joins` — Functional · Could have · Accepted)</span>

        The protocol MAY support queries joining data across multiple storages and external data sources (e.g. SPARQL federation), respecting each source's access control.

        *Rationale:* Joins across pods and public datasets unlock integration use cases but sit atop the simpler query layers.

        *Motivated by:* [Data Integration](#uc-data-integration), [SPARQL Queries](#uc-sparql-queries).

        *Protocol feature(s):* Query and search.

        *Sources:* [#88](https://github.com/w3c/lws-ucs/issues/88)

    1. **<dfn id="req-metadata-query">Metadata Query</dfn>** <span class="informative">(`REQ-metadata-query` — Functional · Should have · Accepted)</span>

        The protocol SHOULD support queries, respecting access control, over server-maintained data (e.g. on a root container, a nested container, or a resource's metadata).

        *Rationale:* Server-maintained metadata (containment, timestamps, types) is what clients most often need to filter on.

        *Motivated by:* [Search Functionality](#uc-search-functionality).

        *Protocol feature(s):* Query and search.

    1. **<dfn id="req-paginate-filter-sort">Pagination, Filtering and Sorting</dfn>** <span class="informative">(`REQ-paginate-filter-sort` — Functional, Non-functional · Should have · Accepted)</span>

        To handle large result sets, the protocol MUST provide features like pagination, filtering, and sorting of query results, and MAY support standard query languages (such as SPARQL) for advanced semantic queries over the data. This applies equally to protocol-level reads such as retrieving a large container.

        *Rationale:* Unpaginated container listings and result sets fail at real-world sizes (thousands of contained resources).

        *Motivated by:* [Key-Value Mirror with Atomic Hydration](#uc-kv-mirror-hydrate), [Pagination & Filtering](#uc-pagination-filtering), [Search Functionality](#uc-search-functionality), [SPARQL Queries](#uc-sparql-queries).

        *Protocol feature(s):* Query and search.

        *Sources:* [#103](https://github.com/w3c/lws-ucs/issues/103)

    1. **<dfn id="req-pod-level-query">Pod-Level Query</dfn>** <span class="informative">(`REQ-pod-level-query` — Functional · Should have · Accepted)</span>

        The protocol SHOULD support queries (e.g. SPARQL) addressed to a whole storage, respecting access control, to easily find data in potentially large storages.

        *Rationale:* Whole-storage query is the primary discovery surface for large pods.

        *Motivated by:* [Search Functionality](#uc-search-functionality), [SPARQL Queries](#uc-sparql-queries).

        *Protocol feature(s):* Query and search.

        *Sources:* [#45](https://github.com/w3c/lws-ucs/issues/45), [#152](https://github.com/w3c/lws-ucs/issues/152)

    1. **<dfn id="req-query-other-pods">Query Other Storages</dfn>** <span class="informative">(`REQ-query-other-pods` — Functional · Should have · Accepted)</span>

        The protocol SHOULD support querying other entities' storages, respecting their access control.

        *Rationale:* Social and collaborative use cases read across storages; access-control-respecting query is the safe primitive.

        *Motivated by:* [Search Functionality](#uc-search-functionality), [SPARQL Queries](#uc-sparql-queries).

        *Protocol feature(s):* Query and search.

    1. **<dfn id="req-resource-level-query">Resource-Level Query</dfn>** <span class="informative">(`REQ-resource-level-query` — Functional · Should have · Accepted)</span>

        The protocol SHOULD support queries scoped to a single resource or container, respecting access control.

        *Rationale:* Scoped query avoids transferring whole resources to extract a fragment.

        *Motivated by:* [Search Functionality](#uc-search-functionality), [SPARQL Queries](#uc-sparql-queries).

        *Protocol feature(s):* Query and search.

1. **<dfn id="req-server-to-server-auth">Server-to-Server Authentication</dfn>** <span class="informative">(`REQ-server-to-server-auth` — Functional, Security · Should have · Accepted)</span>

    The protocol MUST support secure authentication and authorization flows suitable for server-to-server and backend service integration, enabling trusted services to access user storages without interactive login. Possibilities include mutual TLS, signed JWT-based service credentials, and scoped long-lived tokens, among others.

    *Rationale:* Real deployments include headless services (sync daemons, feed readers, indexers) that cannot perform interactive login.

    *Motivated by:* [Backend Service Integration](#uc-backend-service-integration), [Workflow Automation over Storage](#uc-workflow-automation).

    *Protocol feature(s):* Authentication.

    *Sources:* [#40](https://github.com/w3c/lws-ucs/issues/40), [#92](https://github.com/w3c/lws-ucs/issues/92)

1. **<dfn id="req-transfer-of-control">Transfer of Control</dfn>** <span class="informative">(`REQ-transfer-of-control` — Functional · Should have · Accepted)</span>

    The protocol MUST allow an entity to transfer, i.e., irrevocably reassign, control of a storage to another entity.

    *Rationale:* Succession, organisational change and account recovery all require control to move permanently, not just be delegated.

    *Motivated by:* [Delegating Control of a Storage](#uc-delegation-of-control).

    *Protocol feature(s):* Authorization.

1. **<dfn id="req-service-providers">Use of Service Providers</dfn>** <span class="informative">(`REQ-service-providers` — Functional · Should have · Accepted)</span>

    The protocol MUST provide a mechanism by which entities can delegate some functions to trusted service providers. Some interactions might further require a trust relationship between service providers and entities. This MUST NOT impede the ability of an entity to operate or self-host such a service. Trust relationships are not transitive: if an entity trusts a service provider (e.g. an identity provider), no other service provider the entity interacts with is under any obligation to trust it.

    *Rationale:* Decomposition into swappable services (identity, notification, computation) is how the ecosystem stays loosely coupled.

    *Motivated by:* [Trust Mechanism for Storage Providers](#uc-storage-provider-trust).

    *Protocol feature(s):* Extensibility.

    *Sources:* [#127](https://github.com/w3c/lws-ucs/issues/127)

1. **<dfn id="req-collaborative-editing">Collaborative Editing</dfn>** <span class="informative">(`REQ-collaborative-editing` — Functional · Could have · Accepted)</span>

    The protocol MUST define optional mechanisms (e.g., locking, optimistic concurrency, CRDT-based merges) to allow multiple entities to co-author or edit the same resource concurrently, with built-in conflict detection and resolution.

    *Rationale:* Concurrent co-authoring needs protocol-level concurrency primitives; each app inventing its own merge story breaks interoperability.

    *Motivated by:* [CRDT Update Log in Storage](#uc-crdt-collaboration-log), [Semantic Collaboration](#uc-semantic-collaboration).

    *Protocol feature(s):* Concurrency and consistency.

    *Sources:* [#146](https://github.com/w3c/lws-ucs/issues/146)

1. **<dfn id="req-federated-queries">Federated Data Queries</dfn>** <span class="informative">(`REQ-federated-queries` — Functional · Could have · Accepted)</span>

    The protocol MUST support clients performing queries across multiple storages (including federated SPARQL), aggregating and returning results transparently while maintaining each storage's access controls.

    *Rationale:* Cross-storage aggregation is the payoff of decentralised storage; it must not become an access-control bypass.

    *Motivated by:* [Data Integration](#uc-data-integration), [Federated Task Dashboard](#uc-federated-task-dashboard), [SPARQL Queries](#uc-sparql-queries).

    *Protocol feature(s):* Query and search.

    *Sources:* [#88](https://github.com/w3c/lws-ucs/issues/88)

1. **<dfn id="req-profile-interaction-ui">Profile Interaction UI</dfn>** <span class="informative">(`REQ-profile-interaction-ui` — Functional, Interoperability · Could have · Accepted)</span>

    The protocol MUST define a standard method for clients to fetch and display an entity's profile (e.g., WebID), along with supported actions (follow, message, share), so users can engage seamlessly with contacts.

    *Rationale:* A common profile-rendering contract is what makes identities clickable across independently built applications.

    *Motivated by:* [WebID Profile Interaction](#uc-webid-profile-interaction).

    *Protocol feature(s):* Discovery.

    *Sources:* [#47](https://github.com/w3c/lws-ucs/issues/47), [#48](https://github.com/w3c/lws-ucs/issues/48)

1. **<dfn id="req-scalable-storage-management">Scalable Storage Management</dfn>** <span class="informative">(`REQ-scalable-storage-management` — Functional, Non-functional · Could have · Accepted)</span>

    The protocol MUST permit flexible management of an entity's data across multiple storage units or providers, allowing logical unification of disparate back-ends. Clients SHOULD be able to experience a single coherent storage view even if data is split or migrated across providers, supporting scenarios like jurisdictional partitioning or provider failover.

    *Rationale:* Splitting and aggregating storages is how capacity, jurisdiction and failover needs are met without lock-in.

    *Motivated by:* [Storage Flexibility](#uc-storage-flexibility).

    *Protocol feature(s):* Operations.

    *Sources:* [#110](https://github.com/w3c/lws-ucs/issues/110), [#136](https://github.com/w3c/lws-ucs/issues/136)

1. **<dfn id="req-website-publication">Self-Describing Website Publication</dfn>** <span class="informative">(`REQ-website-publication` — Functional · Could have · Accepted)</span>

    The protocol MUST support publication of self-describing websites with persistent URIs directly from a storage, enabling durable, interoperable content hosting.

    *Rationale:* Public web publishing from user-controlled storage keeps content addressable independent of any hosting platform.

    *Motivated by:* [Website Creation](#uc-website-creation).

    *Protocol feature(s):* Resource management.

    *Sources:* [#31](https://github.com/w3c/lws-ucs/issues/31)

1. **<dfn id="req-timeseries">Timeseries Data Support</dfn>** <span class="informative">(`REQ-timeseries` — Functional · Could have · Accepted)</span>

    The protocol MUST include primitives for storing, querying, and aggregating time series resources, supporting configurable resolution limits and multidimensional analysis for data like IoT streams or metrics.

    *Rationale:* High-frequency append-heavy data has access patterns (windowing, downsampling) generic resources do not serve.

    *Motivated by:* [Timeseries Storage](#uc-timeseries-storage).

    *Protocol feature(s):* Query and search.

    *Sources:* [#6](https://github.com/w3c/lws-ucs/issues/6)

1. **<dfn id="req-view-based-sharing">View-Based Data Sharing</dfn>** <span class="informative">(`REQ-view-based-sharing` — Functional, Privacy · Could have · Accepted)</span>

    The protocol MUST enable controllers to define and expose derived 'views' of a resource (e.g., filtered, aggregated, or redacted subsets) such that recipients see only the authorized slice without duplicating the underlying data.

    *Rationale:* Granularity-appropriate sharing without duplication: consumers get the slice they need, never a copy of the whole.

    *Motivated by:* [Sensor Data Sharing](#uc-sensor-data-sharing).

    *Protocol feature(s):* Query and search.

    *Sources:* [#63](https://github.com/w3c/lws-ucs/issues/63), [#106](https://github.com/w3c/lws-ucs/issues/106), [#116](https://github.com/w3c/lws-ucs/issues/116)

1. **<dfn id="req-cors-browser-access">Browser Access from Foreign Origins</dfn>** <span class="informative">(`REQ-cors-browser-access` — Interoperability · Must have · Proposed)</span>

    In its HTTP binding, the protocol MUST be fully usable by browser-based applications served from origins other than the storage's, for all operations the protocol defines (including authentication flows and notifications). Cross-origin support MUST NOT require per-application server configuration.

    *Rationale:* The app-and-storage-decoupled model IS the cross-origin model: every migrated browser app (linkding, elk) is a foreign origin to the user's storage. A storage that requires registering each app origin server-side re-couples what the charter decouples.

    *Motivated by:* [Migrating an Existing App onto User Storage](#uc-legacy-app-migration).

    *Protocol feature(s):* Extensibility.

    *Sources:* [jeswr/linkding](https://github.com/jeswr/linkding)

1. **<dfn id="req-binary-fidelity">Byte-Exact Non-RDF Resource Fidelity</dfn>** <span class="informative">(`REQ-binary-fidelity` — Functional, Interoperability · Must have · Proposed)</span>

    A non-RDF resource retrieved from storage MUST be byte-identical to the representation that was stored, and its declared content type MUST be preserved. A storage MUST NOT transform, re-serialize, or re-encode non-RDF representations.

    *Rationale:* Applications hash, sign and version their native files; a storage that rewrites bytes breaks them undetectably (the whiteboard fork's scene files and media libraries both depend on exact round-trips).

    *Motivated by:* [Binary Asset with Linked Descriptor](#uc-binary-asset-descriptor), [Media Playback from Storage](#uc-media-streaming).

    *Protocol feature(s):* Resource management.

    *Sources:* [jeswr/excalidraw](https://github.com/jeswr/excalidraw)

1. **<dfn id="req-conditional-requests">Conditional Requests and Optimistic Concurrency</dfn>** <span class="informative">(`REQ-conditional-requests` — Functional, Interoperability · Must have · Proposed)</span>

    Every resource MUST expose a stable version validator that changes exactly when the representation changes. Reads MUST be conditionable on the validator (returning a cheap not-modified answer for an unchanged resource). Writes MUST be conditionable on (a) the validator the client last read — rejecting the write if the resource changed (lost-update protection) — and (b) non-existence, so a create-only write can never overwrite an existing resource. Conditional-failure rejections MUST be distinguishable from authorization and other failures.

    *Rationale:* The single most load-bearing storage primitive across the app corpus: optimistic saves (capnote, access-manager), CRDT logs (actual, y-solid — create-only appends + CAS snapshots), cache revalidation (solid-offline), and fail-closed provisioning all reduce to conditional requests. HTTP has the machinery (ETag, If-Match, If-None-Match); the requirement is that the protocol mandate its coherent support.

    *Motivated by:* [Crawling and Indexing Public Storage Data](#uc-public-index-crawl), [CRDT Update Log in Storage](#uc-crdt-collaboration-log), [Durable Save on Exit](#uc-durable-exit-save), [Fail-Closed Provisioning of App Data](#uc-fail-closed-provisioning), [Key-Value Mirror with Atomic Hydration](#uc-kv-mirror-hydrate), [Offline-First Instant Load](#uc-offline-first-instant-load), [Optimistic, Non-Blocking Saves](#uc-optimistic-concurrency).

    *Protocol feature(s):* Concurrency and consistency.

    *Sources:* [jeswr/actual](https://github.com/jeswr/actual), [jeswr/solid-offline](https://github.com/jeswr/solid-offline)

1. **<dfn id="req-secure-defaults">Fail-Closed Creation Semantics</dfn>** <span class="informative">(`REQ-secure-defaults` — Security · Must have · Proposed)</span>

    The protocol MUST make it possible to create a resource or container together with its access policy such that there is no observable interval in which the new data is accessible more broadly than the requested policy — via atomic create-with-policy, or by newly created resources defaulting to no-broader-than-creator access until a policy is set. Where inheritance would grant broader access, the creating client MUST be able to prevent it from the first instant.

    *Rationale:* Five independent app forks each hand-rolled the same write-policy-first-verify-then-write ritual; a protocol in which the safe order is optional will keep producing exposure windows (financial and health data included).

    *Motivated by:* [Fail-Closed Provisioning of App Data](#uc-fail-closed-provisioning), [Migrating an Existing App onto User Storage](#uc-legacy-app-migration).

    *Protocol feature(s):* Authorization.

    *Sources:* [jeswr/actual](https://github.com/jeswr/actual), [jeswr/miniflux](https://github.com/jeswr/miniflux)

1. **<dfn id="req-scoped-access">Least-Privilege Scoped Credentials</dfn>** <span class="informative">(`REQ-scoped-access` — Security · Must have · Proposed)</span>

    The protocol MUST support issuing a credential whose authority is a server-enforced subset of the granting user's: at minimum restrictable to named containers or resource subtrees and to an operation set (e.g. read-only). The storage — not the client — MUST enforce the scope, and the grantor MUST be able to revoke the credential independently of their other grants.

    *Rationale:* Automation nodes and AI agents currently enforce their own scope guards client-side (n8n-nodes-solid, solid-mcp) — worthless against a compromised or prompt-injected client. Least privilege only exists if the server enforces it.

    *Motivated by:* [AI Agent Access to Storage](#uc-ai-agent-access), [User-Owned Agent Memory](#uc-agent-memory), [Workflow Automation over Storage](#uc-workflow-automation).

    *Protocol feature(s):* Authentication, Authorization.

    *Sources:* [jeswr/n8n-nodes-solid](https://github.com/jeswr/n8n-nodes-solid), [jeswr/solid-mcp](https://github.com/jeswr/solid-mcp)

1. **<dfn id="req-non-leaky-discovery">Non-Leaky Discovery</dfn>** <span class="informative">(`REQ-non-leaky-discovery` — Privacy, Security · Must have · Proposed)</span>

    Discovery mechanisms (data registries, type indexes, capability descriptions, search) MUST NOT disclose the existence, type, or location of data an agent is not authorized to know about; a discovery response MUST be indistinguishable between 'does not exist' and 'exists but not authorized for you'.

    *Rationale:* Existence metadata is data: a leaky index defeats resource-level access control wholesale. This constrains every discovery requirement (self-descriptive APIs, search, indexes) rather than adding a parallel surface.

    *Motivated by:* [Discovering Where Data Lives](#uc-app-data-discovery), [Privacy in Data Discovery](#uc-private-data-discovery).

    *Protocol feature(s):* Discovery.

    *Sources:* [#222](https://github.com/w3c/lws-ucs/issues/222)

1. **<dfn id="req-write-attribution">Attribution of Writes</dfn>** <span class="informative">(`REQ-write-attribution` — Functional, Security · Should have · Proposed)</span>

    The protocol SHOULD record, for each write, the authenticated agent AND the application or delegated credential through which it acted, and expose this attribution to authorized entities — so that data written by an agent acting under delegation is distinguishable from data written by the delegating user directly.

    *Rationale:* Agent-written data (memory items, AI edits) must never masquerade as the user's own hand; this is the auditable-trail requirement's write-side counterpart, mechanised for the agent era.

    *Motivated by:* [AI Agent Access to Storage](#uc-ai-agent-access), [Cross-Application Data Interoperability](#uc-cross-app-interop), [User-Owned Agent Memory](#uc-agent-memory).

    *Protocol feature(s):* Audit and accountability.

    *Sources:* [jeswr/solid-memory](https://github.com/jeswr/solid-memory)

1. **<dfn id="req-authorization-enumeration">Authorization Enumeration</dfn>** <span class="informative">(`REQ-authorization-enumeration` — Functional, Security · Should have · Proposed)</span>

    The protocol SHOULD allow an authorized entity (at minimum the controller) to enumerate, in a bounded number of requests, the effective access grants over a resource or container subtree — who holds which modes over which resources, and whether each grant is direct or inherited.

    *Rationale:* Access review is a security control; if the answer requires a full client-side crawl and re-implementation of inheritance, owners will not audit and over-permissioning persists.

    *Motivated by:* [Discovering Who Has Access](#uc-access-overview).

    *Protocol feature(s):* Audit and accountability, Authorization.

    *Sources:* [#212](https://github.com/w3c/lws-ucs/issues/212)

1. **<dfn id="req-app-data-registry">Data Location Registry</dfn>** <span class="informative">(`REQ-app-data-registry` — Functional, Interoperability, Privacy · Should have · Proposed)</span>

    The protocol MUST define a discoverable registry mechanism by which applications record where data of a given class or shape lives in a storage and find where other applications put theirs, including bootstrap semantics when no registry exists yet. Registry reads MUST be access-controlled and MUST NOT leak the existence of data classes the requesting agent is not authorized to know about.

    *Rationale:* Cross-app interoperability in practice starts with 'where are the user's tasks?'; the type-index pattern answers it but is unspecified in the core protocol, and its privacy constraint (issue #222) must be normative, not folklore.

    *Motivated by:* [Cross-Application Data Interoperability](#uc-cross-app-interop), [Discovering Where Data Lives](#uc-app-data-discovery), [Federated Task Dashboard](#uc-federated-task-dashboard).

    *Protocol feature(s):* Discovery.

    *Sources:* [#222](https://github.com/w3c/lws-ucs/issues/222), [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

1. **<dfn id="req-deletion-signaling">Deletion and Move Signaling</dfn>** <span class="informative">(`REQ-deletion-signaling` — Functional · Should have · Proposed)</span>

    The protocol MUST make deletions (and SHOULD make moves) discoverable after the fact by authorized entities: a client that missed the event MUST be able to distinguish 'deleted' (and, where supported, 'moved, now at X') from 'never existed', e.g. via tombstones, move markers, or a change feed that includes deletions. Erasure obligations MUST be satisfiable: a tombstone MUST NOT be required to retain the deleted content.

    *Rationale:* Without a deletion signal every sync engine has the resurrection bug (rxdb-solid resorts to app-level tombstones); link integrity on move/delete is the same mechanism (issues #195, #171), and record lineage after erasure (#228) is its compliance-grade form.

    *Motivated by:* [Deletion Visibility for Replicas](#uc-replica-deletion-sync), [Institutional Records Provability](#uc-institutional-records), [Markers for Moved or Deleted Resources](#uc-link-preservation), [Renaming / Moving a Resource or Container](#uc-resource-rename-move).

    *Protocol feature(s):* Offline and synchronization.

    *Sources:* [#195](https://github.com/w3c/lws-ucs/issues/195), [jeswr/rxdb-solid](https://github.com/jeswr/rxdb-solid)

1. **<dfn id="req-paired-metadata">Descriptive Metadata Without Touching the Resource</dfn>** <span class="informative">(`REQ-paired-metadata` — Functional · Should have · Proposed)</span>

    The protocol MUST support associating descriptive RDF metadata with a resource (including a non-RDF resource) such that the metadata can be created, read and updated without modifying the described resource's bytes or validator, and is discoverable from the resource.

    *Rationale:* The blob+descriptor split (native artifact plus RDF description) is how binary-centric apps stay discoverable to the rest of the ecosystem; without a standard association, each app invents its own naming convention.

    *Motivated by:* [Binary Asset with Linked Descriptor](#uc-binary-asset-descriptor).

    *Protocol feature(s):* Resource management.

    *Sources:* [jeswr/solid-drawing](https://github.com/jeswr/solid-drawing)

1. **<dfn id="req-permission-introspection">Effective-Permission Introspection</dfn>** <span class="informative">(`REQ-permission-introspection` — Functional · Should have · Proposed)</span>

    The protocol MUST allow a client to learn, cheaply and authoritatively, which operations the currently authenticated agent may perform on a resource (e.g. alongside a read response), without the client re-implementing policy evaluation. The answer MUST reflect the server's actual decision procedure.

    *Rationale:* UIs need affordances that match reality; client-side policy re-evaluation duplicates the server's logic and diverges from it (Pod Manager and the access dashboard both hit this). Complementary to authorization ENUMERATION (who has access): this is 'what may I do here?'.

    *Motivated by:* [Permission-Aware User Interface](#uc-permission-aware-ui).

    *Protocol feature(s):* Authorization.

    *Sources:* [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

1. **<dfn id="req-range-requests">Partial-Content Reads</dfn>** <span class="informative">(`REQ-range-requests` — Functional · Should have · Proposed)</span>

    The protocol MUST support partial-content reads (byte ranges) of large resources, so that clients can seek within media and resume interrupted downloads without re-transferring the whole representation.

    *Rationale:* Seeking in audio/video is a range read; without it media playback from storage re-downloads whole files per seek. The download-side complement of resumable uploads.

    *Motivated by:* [Media Playback from Storage](#uc-media-streaming).

    *Protocol feature(s):* Resource management.

    *Sources:* [jeswr/pod-music](https://github.com/jeswr/pod-music)

1. **<dfn id="req-rate-limit-signaling">Rate-Limit Signaling</dfn>** <span class="informative">(`REQ-rate-limit-signaling` — Non-functional · Should have · Proposed)</span>

    A storage that applies rate limits MUST signal them with a structured response including retry timing, so that well-behaved automated clients (pipelines, crawlers, sync engines) can back off correctly instead of failing opaquely or hammering the server.

    *Rationale:* Automated traffic (workflow fan-outs, index crawls, sync bursts) is normal LWS load, and rate limiting is a legitimate defence (issue #179 requests it) — but undisciplined limiting without signalling just breaks the clients that try to behave.

    *Motivated by:* [Crawling and Indexing Public Storage Data](#uc-public-index-crawl), [Workflow Automation over Storage](#uc-workflow-automation).

    *Protocol feature(s):* Operations.

    *Sources:* [#179](https://github.com/w3c/lws-ucs/issues/179), [jeswr/solid-webid-index](https://github.com/jeswr/solid-webid-index)

1. **<dfn id="req-silent-reauth">Silent Session Continuation</dfn>** <span class="informative">(`REQ-silent-reauth` — Functional, Security · Should have · Proposed)</span>

    The authentication mechanism MUST support non-interactive continuation of a previously consented session: a client holding a persistable credential from an earlier interactive login MUST be able to obtain fresh short-lived credentials without user interaction, redirects, or hidden-frame tricks. Such credentials MUST be scoped to the authenticated user, individually revocable, and refused after revocation; higher-sensitivity operations MAY require interactive step-up.

    *Rationale:* Session restore was re-implemented (and re-broken) in every suite app until extracted into a shared library — evidence the capability belongs in the protocol contract (with issues #41/#49 asking for exactly this), not in per-app heroics.

    *Motivated by:* [Authentication Mechanism(s)](#uc-authentication-mechanisms), [Silent Session Restore](#uc-silent-session-restore).

    *Protocol feature(s):* Authentication.

    *Sources:* [#41](https://github.com/w3c/lws-ucs/issues/41), [#49](https://github.com/w3c/lws-ucs/issues/49), [jeswr/solid-session-restore](https://github.com/jeswr/solid-session-restore)

1. **<dfn id="req-app-identity">Stable, Verifiable Application Identity</dfn>** <span class="informative">(`REQ-app-identity` — Interoperability, Security · Should have · Proposed)</span>

    The protocol MUST support a stable, dereferenceable application identifier presenting verifiable metadata (name, operator, redirect endpoints), such that consent prompts can display the actual application, grants can be keyed to it and individually revoked, and the same application is recognizable across sessions. Distinct deployments (origins) of an application MUST be distinguishable where they change the trust context.

    *Rationale:* Anonymous throwaway client registrations make consent meaningless and grant lists unreviewable; stable app identity is also what authorization-by-application (restricting client access, issue #147) presupposes.

    *Motivated by:* [Migrating an Existing App onto User Storage](#uc-legacy-app-migration), [Recognizable Application Identity](#uc-recognizable-app-identity).

    *Protocol feature(s):* Identity.

    *Sources:* [#147](https://github.com/w3c/lws-ucs/issues/147), [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

1. **<dfn id="req-structured-errors">Structured, Machine-Actionable Errors</dfn>** <span class="informative">(`REQ-structured-errors` — Functional, Interoperability · Should have · Proposed)</span>

    Error responses MUST carry a structured, machine-readable representation (e.g. RFC 9457 problem details) identifying the failure class — at minimum distinguishing authentication, authorization, validation, version-conflict, quota, and rate-limit failures — so applications can branch, retry or surface actionable messages. Error detail MUST NOT leak information the requester is not authorized to learn.

    *Rationale:* The existing clear-error-messages story has no requirement in the current document; every consumer (optimistic-save revert logic, workflow branch nodes, quota warnings) needs the failure CLASS, which free-text cannot provide.

    *Motivated by:* [Clear Error Messages](#uc-clear-error-messages), [Optimistic, Non-Blocking Saves](#uc-optimistic-concurrency), [Storage Usage and Quota Insight](#uc-storage-usage-insight), [Workflow Automation over Storage](#uc-workflow-automation).

    *Protocol feature(s):* Operations.

    *Sources:* [#34](https://github.com/w3c/lws-ucs/issues/34), [jeswr/n8n-nodes-solid](https://github.com/jeswr/n8n-nodes-solid)

1. **<dfn id="req-external-identifier-access">Access to Data About External Identifiers</dfn>** <span class="informative">(`REQ-external-identifier-access` — Functional, Interoperability · Could have · Proposed)</span>

    The protocol SHOULD provide a mechanism to store, and to request from a given storage, the data that storage holds about an identifier whose canonical location is elsewhere, without requiring a new identifier to be minted for the local description.

    *Rationale:* Annotation of the web under original identifiers is core linked-data practice; forcing local re-identification breaks the graph.

    *Motivated by:* [Local Data About Foreign Identifiers](#uc-foreign-identifier-data).

    *Protocol feature(s):* Query and search.

    *Sources:* [#215](https://github.com/w3c/lws-ucs/issues/215)

1. **<dfn id="req-atomic-batch">Atomic Multi-Resource Operations</dfn>** <span class="informative">(`REQ-atomic-batch` — Functional · Could have · Proposed)</span>

    The protocol SHOULD provide a mechanism to read a set of resources as one consistent point-in-time view, and MAY provide all-or-nothing application of a set of writes, so that clients restoring or migrating multi-resource state never observe or produce a torn half-state.

    *Rationale:* The Elk fork's restore path had to be hardened into a client-side staged all-or-nothing hydrate; a batch/consistency primitive would make that guarantee a protocol property rather than per-app discipline. Kept SHOULD/MAY: it is in tension with stateless horizontal scaling and must not become a distributed-transaction mandate.

    *Motivated by:* [Key-Value Mirror with Atomic Hydration](#uc-kv-mirror-hydrate).

    *Protocol feature(s):* Concurrency and consistency.

    *Sources:* [jeswr/elk](https://github.com/jeswr/elk)

1. **<dfn id="req-extension-endpoints">Discoverable Extension Endpoints</dfn>** <span class="informative">(`REQ-extension-endpoints` — Functional, Interoperability · Could have · Proposed)</span>

    The protocol MAY define a mechanism by which a storage controller registers additional, discoverable API endpoints (possibly served by third parties) under their storage, such that clients can discover, authenticate to, and verify the owner's endorsement of these endpoints; the mechanism MUST NOT weaken the access control of ordinary resources.

    *Rationale:* One sanctioned extension point absorbs a family of 'add feature X to the server' requests without bloating the core protocol.

    *Motivated by:* [User-Defined Custom API Endpoints](#uc-custom-api-endpoints).

    *Protocol feature(s):* Extensibility.

    *Sources:* [#207](https://github.com/w3c/lws-ucs/issues/207)

1. **<dfn id="req-immutable-snapshots">Immutable Resource Snapshots</dfn>** <span class="informative">(`REQ-immutable-snapshots` — Functional, Security · Could have · Proposed)</span>

    The protocol SHOULD allow a storage to designate a resource as an immutable snapshot: once written it MUST NOT be overwritten or edited, only superseded by a new resource carrying a reference to its predecessor; supersession chains MUST be traversable by authorized entities.

    *Rationale:* Provable records need write-once semantics the generic update model cannot express; versioning alone does not forbid in-place mutation.

    *Motivated by:* [Institutional Records Provability](#uc-institutional-records).

    *Protocol feature(s):* Resource management.

    *Sources:* [#228](https://github.com/w3c/lws-ucs/issues/228)

1. **<dfn id="req-indexing-control">Indexing Control</dfn>** <span class="informative">(`REQ-indexing-control` — Functional · Could have · Proposed)</span>

    The protocol SHOULD provide a way to declare, at resource or container granularity, whether data is intended for indexing and discovery by other consumers, and indexing services SHOULD honour the declaration.

    *Rationale:* Discovery quality degrades fast when internal representations pollute indexes; the CRDT-log pattern in real local-first apps makes this concrete.

    *Motivated by:* [Crawling and Indexing Public Storage Data](#uc-public-index-crawl), [CRDT Update Log in Storage](#uc-crdt-collaboration-log), [Indexed and Non-Indexed Data](#uc-selective-indexing).

    *Protocol feature(s):* Discovery.

    *Sources:* [#208](https://github.com/w3c/lws-ucs/issues/208)

1. **<dfn id="req-pseudonymity">Pseudonymous Identifiers</dfn>** <span class="informative">(`REQ-pseudonymity` — Privacy · Could have · Proposed)</span>

    The protocol SHOULD allow an entity to present distinct, unlinkable pseudonymous identifiers to distinct relying parties (and to rotate them over time), such that access still authorizes correctly but relying parties cannot correlate the entity across contexts via the identifier or storage location.

    *Rationale:* Stable global identifiers are a tracking vector by construction; pseudonymity is the standing mitigation and interacts with the profile-management requirement (one persona per context) without replacing it.

    *Motivated by:* [Pseudonymous Access for Vendors](#uc-pseudonymous-access).

    *Protocol feature(s):* Identity.

    *Sources:* [#195](https://github.com/w3c/lws-ucs/issues/195)

1. **<dfn id="req-rename-move">Server-Side Rename and Move</dfn>** <span class="informative">(`REQ-rename-move` — Functional · Could have · Proposed)</span>

    The protocol SHOULD support renaming or moving a resource or container (including its contents) as a server-side operation that does not require re-transferring content, and SHOULD define how inbound references to the old identifier behave afterwards.

    *Rationale:* Reorganisation is routine data management; client-side copy-then-delete is quadratically expensive and loses metadata and grants.

    *Motivated by:* [Renaming / Moving a Resource or Container](#uc-resource-rename-move).

    *Protocol feature(s):* Resource management.

    *Sources:* [#171](https://github.com/w3c/lws-ucs/issues/171)

1. **<dfn id="req-write-validation">Server-Side Write Validation</dfn>** <span class="informative">(`REQ-write-validation` — Functional, Security · Could have · Proposed)</span>

    The protocol SHOULD allow a resource controller to associate validation rules (e.g., shapes or conditions over the mutation and the authenticated agent) with a resource, such that mutating requests not satisfying the rules are rejected with a structured error before any change is applied.

    *Rationale:* Append-capable shared resources (groups, inboxes) are otherwise spam- and spoof-prone; client-side discipline cannot secure a multi-writer resource.

    *Motivated by:* [Custom Validation of Mutating Requests](#uc-mutation-validation).

    *Protocol feature(s):* Resource management.

    *Sources:* [#93](https://github.com/w3c/lws-ucs/issues/93)

1. **<dfn id="req-quota-discovery">Usage and Quota Discovery</dfn>** <span class="informative">(`REQ-quota-discovery` — Functional · Could have · Proposed)</span>

    The storage description SHOULD expose machine-readable usage and quota information (total used, limit if any, and per-container aggregate size on request), and a write rejected for quota reasons MUST be signalled with a structured, distinguishable error.

    *Rationale:* Storage management UIs cannot render a usage view by crawling the tree, and apps cannot pre-empt quota failures they cannot see coming.

    *Motivated by:* [Storage Usage and Quota Insight](#uc-storage-usage-insight).

    *Protocol feature(s):* Operations.

    *Sources:* [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

1. **<dfn id="req-usage-control">Usage Control Policies</dfn>** <span class="informative">(`REQ-usage-control` — Functional, Privacy · Could have · Proposed)</span>

    The protocol SHOULD support policies expressing usage conditions beyond access — notably the purpose of use — such that a requesting party can declare its intended usage, the policy decision can evaluate that declaration, and the recipient receives a verifiable attestation of the usage that was authorized.

    *Rationale:* Purpose limitation is a core data-protection principle (and the heart of the #59–#86 usage-control issue cluster); technically it composes with, rather than replaces, access control.

    *Motivated by:* [Consent-Based Sharing](#uc-consent-based-sharing), [Indexing a Volunteer Profile](#uc-profile-indexing), [Usage Control](#uc-usage-control).

    *Protocol feature(s):* Authorization.

    *Sources:* [#59](https://github.com/w3c/lws-ucs/issues/59), [#66](https://github.com/w3c/lws-ucs/issues/66), [#82](https://github.com/w3c/lws-ucs/issues/82)

1. **<dfn id="req-verified-references">Verified References to External Resources</dfn>** <span class="informative">(`REQ-verified-references` — Functional, Security · Could have · Proposed)</span>

    The protocol SHOULD support storing a typed reference to an external resource consisting of its identifier and a content hash, without copying the payload, such that a client can verify at link time — and re-verify on demand — that the referenced content still matches the hash.

    *Rationale:* Reference-not-copy with cryptographic pinning is what lets a personal storage aggregate institution-held records without becoming a second source of truth.

    *Motivated by:* [Institutional Records Provability](#uc-institutional-records).

    *Protocol feature(s):* Encryption, Resource management.

    *Sources:* [#228](https://github.com/w3c/lws-ucs/issues/228)
