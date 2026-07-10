<!-- GENERATED from ucr/*.ttl by scripts/generate-spec-md.py — DO NOT EDIT BY HAND.
     Edit the Turtle corpus and regenerate (python3 scripts/generate-spec-md.py). -->

The use cases below are generated from the machine-readable corpus in [`ucr/`](https://github.com/jeswr/lws-ucs/tree/main/ucr), expressed with the [`lws-ucr` ontology](https://github.com/jeswr/lws-ucs/blob/main/docs/ontology.md) and validated by its SHACL shapes: every use case has a stable identifier, a primary actor from the shared role scheme, and a machine-checked link to the requirements it motivates. Items marked **Accepted** come from the previously published document; items marked **Proposed** are new submissions (from open issue triage or derived from deployed applications) awaiting WG review.

## Functional Stories

### Data management

- **<dfn id="uc-generic-storage">Generic Storage</dfn>** <span class="informative">(`UC-generic-storage` — Accepted)</span>

  **As an** user, **I want** a format-agnostic online storage system that supports any type of resource, so I can perform create, read, update and delete — including metadata and access-control modifications, and recovery of previous versions — from any device at any time, **so that** I have seamless data management across devices and full control over my resources.

  *Context:* The foundational storage story: any resource type, full CRUD including metadata and access-control state, version recovery, device-independent.

  *Derived requirements:* [Adding, Updating, Deleting Resources in Storage](#req-resource-crud), [Resource Versioning](#req-resource-versioning).

  *Sources:* [#60](https://github.com/w3c/lws-ucs/issues/60), [#62](https://github.com/w3c/lws-ucs/issues/62), [#63](https://github.com/w3c/lws-ucs/issues/63), [#69](https://github.com/w3c/lws-ucs/issues/69), [#97](https://github.com/w3c/lws-ucs/issues/97), [#117](https://github.com/w3c/lws-ucs/issues/117)

- **<dfn id="uc-large-file-uploads">Large File Uploads</dfn>** <span class="informative">(`UC-large-file-uploads` — Accepted)</span>

  **As an** user, **I want** to upload very large files to my storage, resuming an interrupted transfer where it left off, **so that** an unreliable connection never forces a multi-gigabyte transfer to restart from zero.

  *Context:* Uploads of large media (video, disk images, sensor archives) routinely exceed the reliability window of consumer connections; without resumability the probability of ever completing a transfer falls with file size.

  *Preconditions:* The actor is authenticated and authorized to create the target resource. The storage advertises resumable-upload support in its storage description.

  *Main flow:*
    1. The user's application begins uploading a 4 GB video to a container in their storage.
    2. The connection drops at 60% transferred.
    3. On reconnect, the application asks the server which bytes were durably received.
    4. The application resumes the transfer from that offset.
    5. The server completes creation of the resource exactly once and reports success.

  *Error flow:* If the partial upload has expired before resumption, the server reports it as no longer resumable; the application restarts cleanly. No partially transferred bytes are ever observable at the target URI.

  *Postconditions:* The resource exists in the storage byte-identical to the source, and its creation is observable exactly once (e.g. to notification subscribers).

  *Derived requirements:* [Resumable Large Data Transfers](#req-resumable-uploads).

  *Sources:* [#18](https://github.com/w3c/lws-ucs/issues/18)

- **<dfn id="uc-offline-data-access">Offline Data Access</dfn>** <span class="informative">(`UC-offline-data-access` — Accepted)</span>

  **As an** user, **I want** to access and modify my data offline, with automatic synchronization upon reconnection, **so that** I can work without a network and avoid data corruption or conflicts.

  *Context:* Offline support is vital for users in areas with unreliable connectivity.

  *Derived requirements:* [Offline Access and Synchronization](#req-offline-sync).

  *Sources:* [#64](https://github.com/w3c/lws-ucs/issues/64), [#65](https://github.com/w3c/lws-ucs/issues/65), [#67](https://github.com/w3c/lws-ucs/issues/67), [#138](https://github.com/w3c/lws-ucs/issues/138)

- **<dfn id="uc-storage-portability">Portable Storage</dfn>** <span class="informative">(`UC-storage-portability` — Accepted)</span>

  **As an** user, **I want** to move my storage between providers, or self-host it, without losing data, identifiers, or standing access arrangements, **so that** I am never locked in: my data, its addresses, and the grants I have made survive a change of provider.

  *Context:* Data sovereignty is a founding motivation of LWS. Portability is only real if a move preserves not just the bytes but the web around them: long-lived authorizations (a patient's drug-interaction agent must keep access across a move — issue #164) and published public resources (a journalist's documents must remain retrievable after their publisher account is rescinded — issue #165).

  *Preconditions:* The user controls a globally unique storage identity independent of the current provider.

  *Main flow:*
    1. The user initiates a transfer of their storage from provider A to provider B (or to self-hosting).
    2. The complete storage — resources, metadata, and access-control state — is transferred.
    3. The user verifies the imported data is authentic and complete.
    4. Identifiers resolve to the new location; provider A is released of responsibility.

  *Alternative flow:* A patient moves storage providers. Their pharmacy's drug-interaction agent, granted read access to the medication list years earlier, continues to operate across the move without re-authorization (from issue #164).

  *Alternative flow:* A journalist's published public documents remain retrievable after their account at the original publisher is rescinded (from issue #165).

  *Postconditions:* All resources are available at the new location with integrity verifiable against the source. Long-lived access grants continue to authorize the same parties after the move. Previously published public resources remain retrievable. The former provider is released of responsibility for the moved storage.

  *Derived requirements:* [Storage Portability](#req-storage-portability).

  *Sources:* [#30](https://github.com/w3c/lws-ucs/issues/30), [#164](https://github.com/w3c/lws-ucs/issues/164), [#165](https://github.com/w3c/lws-ucs/issues/165)

- **<dfn id="uc-binary-asset-descriptor">Binary Asset with Linked Descriptor</dfn>** <span class="informative">(`UC-binary-asset-descriptor` — Proposed)</span>

  **As an** application developer, **I want** to store an application's native binary or JSON artifact byte-exactly, with a small linked RDF descriptor carrying the metadata other apps need, **so that** the owning app round-trips its file with full fidelity while other apps can still discover, list and describe it without parsing the native format.

  *Context:* The whiteboard fork (jeswr/excalidraw with the jeswr/solid-drawing model) stores each scene as the app's native file — which MUST round-trip byte-identical, or the app's own hashing/versioning breaks — paired with an RDF descriptor (title, thumbnail, schema version, pointer to the blob). The storage must (a) preserve non-RDF representations exactly as written, including content type, and (b) support associating descriptor metadata with a resource without touching its bytes. The same split recurs for media libraries and document stores.

  *Postconditions:* A retrieved binary resource is byte-identical to what was stored, with the content type preserved.

  *Derived requirements:* [Byte-Exact Non-RDF Resource Fidelity](#req-binary-fidelity), [Descriptive Metadata Without Touching the Resource](#req-paired-metadata).

  *Sources:* [jeswr/excalidraw](https://github.com/jeswr/excalidraw), [jeswr/solid-drawing](https://github.com/jeswr/solid-drawing)

- **<dfn id="uc-crdt-collaboration-log">CRDT Update Log in Storage</dfn>** <span class="informative">(`UC-crdt-collaboration-log` — Proposed)</span>

  **As an** application developer, **I want** to persist a CRDT document as an append-only log of update resources plus a periodically compacted snapshot, with the storage as the sole synchronization point, **so that** multiple devices and collaborators converge without a dedicated sync server, without read-modify-write races, and crash/offline-safely.

  *Context:* Two independent implementations converged on the same storage shape: a budgeting app's sync backend (jeswr/actual — an HLC-keyed append-only message log plus a merkle snapshot updated by compare-and-swap) and a Yjs persistence provider (jeswr/y-solid — binary update log plus compact()). The pattern needs: create-only writes (a new log entry must never overwrite an existing one), conditional snapshot replacement (CAS with retry), ordered container listing to replay the log, and a way to mark the log as internal non-indexable structure. Storage-level conflict handling is unnecessary — the CRDT semantics make appends commutative — but the primitives must not get in the way.

  *Preconditions:* The application's data type is CRDT-mergeable (appends commute).

  *Main flow:*
    1. Each device appends its local CRDT updates as new create-only resources in a log container.
    2. On sync, a device lists the log container, fetches entries it has not seen, and merges them (idempotently — re-merging is safe).
    3. Periodically a device writes a compacted snapshot with a conditional replace, retrying on concurrent modification, then garbage-collects folded log entries.
    4. The log container is marked as internal structure so indexers skip it.

  *Postconditions:* Two replicas that each appended offline converge after both synchronize, with no lost updates.

  *Derived requirements:* [Collaborative Editing](#req-collaborative-editing), [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Indexing Control](#req-indexing-control).

  *Sources:* [jeswr/actual](https://github.com/jeswr/actual), [jeswr/y-solid](https://github.com/jeswr/y-solid)

- **<dfn id="uc-replica-deletion-sync">Deletion Visibility for Replicas</dfn>** <span class="informative">(`UC-replica-deletion-sync` — Proposed)</span>

  **As an** application developer, **I want** a replica that was offline to learn which resources were deleted while it was away, **so that** deletions propagate to every replica instead of silently resurrecting on the next push.

  *Context:* A replication engine (jeswr/rxdb-solid, an RxDB replication plugin) cannot distinguish 'deleted upstream' from 'never existed' by observing absence: if a replica missed the deletion, its next push recreates the resource (the resurrection bug). The plugin resorts to app-level tombstone resources because the storage exposes no deletion signal. A protocol-level answer — tombstones, a deletion feed, or since-token change listing including deletes — serves every sync engine at once. Move markers (issue #195) are the same mechanism for renames.

  *Error flow:* Device A deletes a document and syncs. Device B, offline during the deletion, comes back and pushes its full local set; the deleted document reappears for everyone. The deletion signal exists precisely to make this resurrection impossible.

  *Derived requirements:* [Deletion and Move Signaling](#req-deletion-signaling), [Offline Access and Synchronization](#req-offline-sync).

  *Sources:* [jeswr/rxdb-solid](https://github.com/jeswr/rxdb-solid)

- **<dfn id="uc-durable-exit-save">Durable Save on Exit</dfn>** <span class="informative">(`UC-durable-exit-save` — Proposed)</span>

  **As an** application developer, **I want** the final state of a document to be persisted reliably when the user closes the tab or app, within the tiny time budget the platform allows, **so that** closing the lid never loses the last minutes of work.

  *Context:* Browsers give a closing page milliseconds and a strict payload budget (keepalive requests) for last-moment writes. The whiteboard fork (jeswr/excalidraw) implements a size-gated keepalive save with in-flight deduplication and clear-on-success. For this to work against a storage, small writes must be cheap (no multi-round-trip handshake on the hot path) and their success observable. This is a performance-envelope requirement on the write path, not a new primitive.

  *Derived requirements:* [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Performance and Scalability](#req-performance-scalability).

  *Sources:* [jeswr/excalidraw](https://github.com/jeswr/excalidraw)

- **<dfn id="uc-institutional-records">Institutional Records Provability</dfn>** <span class="informative">(`UC-institutional-records` — Proposed)</span>

  **As a** data owner, **I want** institutional records (permits, medical records, legal decisions) to be stored as verifiably attributable, version-frozen, cryptographically sealed snapshots — and citizens to hold verified references to them in their own storages, **so that** a decision is provable in a legal dispute years later, and a citizen can maintain a self-controlled, verifiable view of their own affairs across institutional boundaries without central registries.

  *Context:* Two complementary halves. Institution-side: a finalized record is sealed as an immutable snapshot (superseded, never overwritten), attributable to the responsible party, with payload deletion possible for the right to erasure while the record's existence and lineage survive as a tombstone. Citizen-side: the citizen's storage holds typed references (identifier + content hash) to institution-held records — not copies — verifiable at link time and re-verifiable on demand, shareable selectively, and aggregable into a named case whose completeness is itself provable.

  *Other actors:* auditor, user.

  *Main flow:*
    1. A civil servant finalizes a building-permit decision; the institution's storage seals it as an immutable, attributable snapshot.
    2. The affected citizen links a verified reference (identifier plus content hash) to the snapshot into their own storage.
    3. Three years later the citizen presents the reference in a dispute; the relying party resolves it and verifies the hash matches the sealed snapshot.
    4. The citizen exercises their right to erasure over the personal payload; the record's existence, metadata and lineage remain as a tombstone.

  *Postconditions:* Any relying party can verify a referenced record is byte-identical to the sealed snapshot the institution finalized. Erasure of a record's payload preserves the record's existence, metadata and lineage.

  *Derived requirements:* [Data Integrity Verification](#req-data-integrity-verification), [Deletion and Move Signaling](#req-deletion-signaling), [Immutable Resource Snapshots](#req-immutable-snapshots), [Verified References to External Resources](#req-verified-references).

  *Sources:* [#228](https://github.com/w3c/lws-ucs/issues/228)

- **<dfn id="uc-kv-mirror-hydrate">Key-Value Mirror with Atomic Hydration</dfn>** <span class="informative">(`UC-kv-mirror-hydrate` — Proposed)</span>

  **As an** application developer, **I want** to mirror an app's key-value state (settings, drafts, small documents) as many small resources under a container, and to restore it on a new device as one consistent snapshot, **so that** any KV-shaped app gains pod persistence with no schema work, and a restore never applies a torn half-state.

  *Context:* The KV-over-storage pattern appears twice independently: a generic unstorage driver (jeswr/unstorage-solid) mapping get/set/keys onto resources and container listings, and the Elk social client (jeswr/elk) mirroring its settings/drafts, whose restore path had to be hardened into an ATOMIC staged-batch hydrate — fetch all entries first, apply all-or-nothing — because applying entries one by one left the app in a torn state when a fetch failed mid-restore. Needs: efficient enumeration of container members (with pagination at size), cheap many-small-resource reads, and ideally batch or at-least-consistent multi-resource read semantics.

  *Main flow:*
    1. On login on a new device, the app lists the KV container and stages every entry locally without applying any.
    2. Only when every entry is fetched does the app apply the whole batch to its state in one step.
    3. Ongoing writes mirror individual keys as create-or-replace of individual resources.
    4. A failed restore leaves the prior local state untouched.

  *Postconditions:* After hydration the local state equals a single point-in-time view of the mirrored container — never a mixture of two states.

  *Derived requirements:* [Atomic Multi-Resource Operations](#req-atomic-batch), [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Pagination, Filtering and Sorting](#req-paginate-filter-sort).

  *Sources:* [jeswr/elk](https://github.com/jeswr/elk), [jeswr/unstorage-solid](https://github.com/jeswr/unstorage-solid)

- **<dfn id="uc-foreign-identifier-data">Local Data About Foreign Identifiers</dfn>** <span class="informative">(`UC-foreign-identifier-data` — Proposed)</span>

  **As an** user, **I want** to store and retrieve data in my storage about an identifier whose canonical location is a different storage (a friend's WebID, a remote ontology), **so that** I can keep information I own about external entities under their own identifier — no invented duplicate identifiers — and still reach the canonical source.

  *Context:* Bob keeps notes about Alice under Alice's own identifier; a service caches ontologies whose original hosting lapsed under their original IRIs. The storage must support retrieving what a storage says about an identifier it does not host (distinct from dereferencing the identifier itself), preserving interoperability of the original IRI.

  *Derived requirements:* [Access to Data About External Identifiers](#req-external-identifier-access).

  *Sources:* [#215](https://github.com/w3c/lws-ucs/issues/215)

- **<dfn id="uc-link-preservation">Markers for Moved or Deleted Resources</dfn>** <span class="informative">(`UC-link-preservation` — Proposed)</span>

  **As an** user, **I want** moved or deleted resources to leave a discoverable marker, **so that** existing links do not silently break when data moves within a provider or migrates to another one.

  *Context:* Linked data is built on links; a move or delete without a marker severs every inbound reference indistinguishably from a network error. A marker (tombstone for deletions, forwarding marker for moves) lets clients distinguish gone from moved from never-existed. Cf. pdsinterop's solid-link-metadata as prior art.

  *Other actors:* application developer.

  *Derived requirements:* [Deletion and Move Signaling](#req-deletion-signaling).

  *Sources:* [#195](https://github.com/w3c/lws-ucs/issues/195)

- **<dfn id="uc-media-streaming">Media Playback from Storage</dfn>** <span class="informative">(`UC-media-streaming` — Proposed)</span>

  **As an** user, **I want** to play music and video, and browse large photo collections, directly from my storage, **so that** my media library lives with me, not with a streaming platform, and still seeks, scrubs and thumbnails like one.

  *Context:* Media apps over pods (the pod-music and pod-photos apps) need partial-content reads: seeking in an audio or video file is a byte-range request, not a full download; a photo grid needs to fetch many images efficiently. Without range support a seek re-downloads the file — unusable on large media. Derived representations (thumbnails, transcodes) also want a home that does not disturb the original (see the linked-descriptor use case).

  *Other actors:* application developer.

  *Derived requirements:* [Byte-Exact Non-RDF Resource Fidelity](#req-binary-fidelity), [Partial-Content Reads](#req-range-requests).

  *Sources:* [jeswr/pod-music](https://github.com/jeswr/pod-music), [jeswr/pod-photos](https://github.com/jeswr/pod-photos)

- **<dfn id="uc-offline-first-instant-load">Offline-First Instant Load</dfn>** <span class="informative">(`UC-offline-first-instant-load` — Proposed)</span>

  **As an** application developer, **I want** my app to paint instantly from a durable local cache and revalidate against the storage cheaply in the background, **so that** users never see a blank loading screen when a cache exists, online or offline, and revalidation costs almost nothing when nothing changed.

  *Context:* The stale-while-revalidate pattern every offline-first app converges on (implemented in solid-offline as a service-worker layer): hydrate synchronously from cache, then revalidate. It depends on storage-side primitives — stable validators (ETags) so a conditional read of an unchanged resource costs a 304 and no body, and change notifications so caches are invalidated by push instead of blind polling.

  *Other actors:* user.

  *Main flow:*
    1. The user reopens the app; it renders synchronously from its durable local cache.
    2. In the background the app revalidates cached resources with conditional reads; unchanged resources return only a not-modified signal.
    3. The app subscribes to change notifications for the resources it caches; a push invalidates exactly the changed entries.
    4. Offline, the app serves the cache and queues writes for synchronization.

  *Postconditions:* Reopening the app with a warm cache renders immediately; a subsequent conditional read transfers no body when the resource is unchanged.

  *Derived requirements:* [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Offline Access and Synchronization](#req-offline-sync), [Subscribing to Resource Changes (Notifications)](#req-change-notifications).

  *Sources:* [jeswr/solid-offline](https://github.com/jeswr/solid-offline)

- **<dfn id="uc-optimistic-concurrency">Optimistic, Non-Blocking Saves</dfn>** <span class="informative">(`UC-optimistic-concurrency` — Proposed)</span>

  **As an** application developer, **I want** user actions to update the interface immediately and persist asynchronously, with lost-update protection when the same resource changed underneath, **so that** the app feels instant, yet two writers (or two tabs) can never silently overwrite each other's changes.

  *Context:* The standing UX invariant across the suite's apps (capital-notes, Pod Manager, solid-access-manager): mutate the UI at once, write behind a small saving indicator, and on write failure revert and explain. It is only safe if every replace can be made conditional on the version the client read (compare-and-swap via validators), and only implementable if the version-conflict rejection is structured enough to distinguish 'conflict — refetch and retry' from other failures. Access-control edits raise the stakes: solid-access-manager applies revocations with CAS specifically so concurrent policy edits cannot resurrect a revoked grant.

  *Other actors:* user.

  *Error flow:* Two tabs edit the same resource. Tab A saves first; tab B's conditional replace is rejected because the version it read is stale. Tab B refetches, reapplies the user's change over the new state (or surfaces a merge prompt), and retries. Without the conditional-write rejection, tab B would silently destroy tab A's save.

  *Derived requirements:* [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Structured, Machine-Actionable Errors](#req-structured-errors).

  *Sources:* [jeswr/capnote](https://github.com/jeswr/capnote), [jeswr/solid-access-manager](https://github.com/jeswr/solid-access-manager), [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

- **<dfn id="uc-resource-rename-move">Renaming / Moving a Resource or Container</dfn>** <span class="informative">(`UC-resource-rename-move` — Proposed)</span>

  **As an** user, **I want** to rename or move a resource or container to a different name or location, **so that** I can organize my storage my preferred way (and apps can migrate old layouts to new conventions).

  *Context:* Moving changes the resource's identifier and may break inbound links (including registrations in type indexes); it thus differs from create/modify/delete. Unlike whole-storage portability, relative-URL tricks do not help within a storage. A server-side move must not require re-uploading content — decisive for large resources and containers.

  *Main flow:*
    1. The user renames /journal/movies.ttl to /journal/movie.ttl; the server performs the rename without the content being re-transferred.
    2. The user moves container /journal/images/ to /images/journal/; the container and all contained resources move in one operation.
    3. Clients holding the old identifiers discover the move (e.g. via a move marker or redirect) instead of hitting a silent 404.

  *Postconditions:* The resource is accessible at the new identifier without re-upload; the fate of the old identifier (tombstone, redirect, or nothing) is explicit.

  *Derived requirements:* [Deletion and Move Signaling](#req-deletion-signaling), [Server-Side Rename and Move](#req-rename-move).

  *Sources:* [#171](https://github.com/w3c/lws-ucs/issues/171)

### Access control and sharing

- **<dfn id="uc-administrative-assistant">Administrative Assistant</dfn>** <span class="informative">(`UC-administrative-assistant` — Accepted)</span>

  **As a** data owner, **I want** to delegate a specific subset of my permissions (e.g. calendar management, correspondence screening) to my assistant, **so that** my assistant can act on my behalf within defined bounds while I remain accountable for, and informed of, what was done in my name.

  *Context:* A department head delegates day-to-day handling of their calendar and inbox to an assistant. The assistant must be able to act without receiving the head's full authority, and every delegated action must remain attributable to the assistant while occurring under the head's mandate.

  *Other actors:* delegate.

  *Preconditions:* Both the data owner and the delegate have distinct authenticatable identities. The resources to be delegated (calendar, inbox) reside in the owner's storage.

  *Main flow:*
    1. The department head grants the assistant write access to the calendar container and read access to the correspondence inbox.
    2. The assistant schedules meetings and screens correspondence using an application of their own choice.
    3. The head reviews the audit log and sees each action attributed to the assistant, acting under the head's grant.
    4. When the assistant changes role, the head revokes the delegation; the assistant's access ends immediately.

  *Alternative flow:* The delegate attempts an operation outside the delegated subset (e.g. reading the head's health records); the storage denies it, and the attempt appears in the audit log.

  *Postconditions:* An audit log attributes each delegated action to the delegate acting under the owner's grant. Revoking the delegation immediately withdraws the delegate's access without disturbing other grants. The delegate can perform exactly the delegated operations and no others.

  *Derived requirements:* [Auditable Trail](#req-auditable-trail), [Delegation of Access Rights](#req-delegation-of-access-rights).

  *Sources:* [#10](https://github.com/w3c/lws-ucs/issues/10)

- **<dfn id="uc-context-aware-access-policies">Context-Aware Access Policies</dfn>** <span class="informative">(`UC-context-aware-access-policies` — Accepted)</span>

  **As an** administrator, **I want** to enforce access policies based on contextual factors like time or geolocation or relative location (near Bob), **so that** access to data adapts dynamically to real-world conditions.

  *Context:* Context-aware policies enhance security and flexibility.

  *Derived requirements:* [Contextual Access Control](#req-contextual-access-control).

  *Sources:* [#17](https://github.com/w3c/lws-ucs/issues/17), [#94](https://github.com/w3c/lws-ucs/issues/94), [#147](https://github.com/w3c/lws-ucs/issues/147)

- **<dfn id="uc-delegation-of-control">Delegating Control of a Storage</dfn>** <span class="informative">(`UC-delegation-of-control` — Accepted)</span>

  **As a** data owner, **I want** to delegate control of a storage to another entity — temporarily or permanently — and to transfer control outright when needed, **so that** another party can administer my storage on my behalf (or take it over entirely, e.g. on succession) without my sharing credentials.

  *Context:* RECONSTRUCTED: the requirements document back-referenced a story named 'Delegation of Control' (from both the delegation and transfer-of-control requirements) that did not exist in the stories list — a dangling by-name reference now caught by the machine-checked motivatedBy chain. Whole-storage control delegation is distinct from per-resource access delegation (see the Administrative Assistant use case): it covers administration, policy management, and irrevocable transfer (succession, organisational change).

  *Other actors:* delegate.

  *Derived requirements:* [Delegation of Control](#req-delegation-of-control), [Transfer of Control](#req-transfer-of-control).

  *Sources:* [w3c/lws-ucs/blob/main/spec/requirements.md](https://github.com/w3c/lws-ucs/blob/main/spec/requirements.md)

- **<dfn id="uc-group-sharing">Group Sharing</dfn>** <span class="informative">(`UC-group-sharing` — Accepted)</span>

  **As an** user, **I want** to share data with dynamic groups (e.g., event attendees), **so that** membership and permissions update automatically as the group evolves.

  *Context:* This simplifies access management for temporary or changing collaborations. A group or organization must itself be able to be a data owner (issue #38).

  *Other actors:* collaborator.

  *Derived requirements:* [Data Sharing](#req-data-sharing), [Group-Based Access Control](#req-group-access-control).

  *Sources:* [#38](https://github.com/w3c/lws-ucs/issues/38), [#102](https://github.com/w3c/lws-ucs/issues/102)

- **<dfn id="uc-health-record-access">Health Record Access</dfn>** <span class="informative">(`UC-health-record-access` — Accepted)</span>

  **As an** user, **I want** to share specific health records with an AI assistant using delegated authorization, **so that** I can get a second opinion, with audit logs ensuring accountability.

  *Context:* A patient shares selected health records with an AI assistant under a delegated, audited authorization — secure, accountable health data sharing for informed decisions.

  *Other actors:* autonomous agent, delegate.

  *Derived requirements:* [Access Request Handling](#req-access-request-handling), [Auditable Trail](#req-auditable-trail), [Data Sharing](#req-data-sharing), [Delegation of Access Rights](#req-delegation-of-access-rights).

  *Sources:* [#11](https://github.com/w3c/lws-ucs/issues/11), [#46](https://github.com/w3c/lws-ucs/issues/46), [#54](https://github.com/w3c/lws-ucs/issues/54)

- **<dfn id="uc-permission-change-notifications">Notifications for Permission Changes</dfn>** <span class="informative">(`UC-permission-change-notifications` — Accepted)</span>

  **As a** collaborator, **I want** to receive notifications when my permissions on a resource are granted, revoked, or modified, **so that** I am informed about changes to my access rights in a timely manner.

  *Context:* Timely notifications help collaborators stay updated on their access to shared resources, enhancing collaboration and security. Issue #205 extends this to any agent being alerted when it is added to or removed from access control — including, under attribute-based access control, notifying the attribute's issuer.

  *Derived requirements:* [Subscribing to Resource Changes (Notifications)](#req-change-notifications).

  *Sources:* [#78](https://github.com/w3c/lws-ucs/issues/78), [#116](https://github.com/w3c/lws-ucs/issues/116), [#205](https://github.com/w3c/lws-ucs/issues/205)

- **<dfn id="uc-profile-sharing">Profile Sharing</dfn>** <span class="informative">(`UC-profile-sharing` — Accepted)</span>

  **As an** user, **I want** to maintain multiple profiles with distinct access controls, **so that** I can share specific information while keeping other data private.

  *Context:* Multiple profiles support different personas or contexts (e.g., work vs. personal). Issue #192 asks for this use case to be written out fully in support of the profile-management requirement: the elaboration here — distinct identifiers, metadata namespaces and access-control rules per profile — is that write-up.

  *Main flow:*
    1. The user creates a professional profile exposing employment and contact data, and a personal profile exposing social data.
    2. Each profile has its own identifier and its own access-control rules; the two are not linked by default.
    3. A colleague resolving the professional identifier sees only the professional profile's data.
    4. The user grants a friend access under the personal profile; the friend never learns the professional identifier exists.

  *Derived requirements:* [Data Sharing](#req-data-sharing), [Profile Management](#req-profile-management).

  *Sources:* [#29](https://github.com/w3c/lws-ucs/issues/29), [#57](https://github.com/w3c/lws-ucs/issues/57), [#192](https://github.com/w3c/lws-ucs/issues/192)

- **<dfn id="uc-sharing-access">Sharing Access</dfn>** <span class="informative">(`UC-sharing-access` — Accepted)</span>

  **As a** data owner, **I want** to grant and revoke fine-grained permissions on my resources, **so that** collaborators have appropriate access and receive notifications when their permissions change.

  *Context:* Granular control ensures secure and tailored data sharing.

  *Other actors:* collaborator.

  *Derived requirements:* [Data Sharing](#req-data-sharing).

  *Sources:* [#7](https://github.com/w3c/lws-ucs/issues/7), [#27](https://github.com/w3c/lws-ucs/issues/27), [#98](https://github.com/w3c/lws-ucs/issues/98), [#116](https://github.com/w3c/lws-ucs/issues/116), [#120](https://github.com/w3c/lws-ucs/issues/120), [#148](https://github.com/w3c/lws-ucs/issues/148)

- **<dfn id="uc-access-overview">Discovering Who Has Access</dfn>** <span class="informative">(`UC-access-overview` — Proposed)</span>

  **As a** data owner, **I want** to see which users and applications hold read/write/append access to resources in my storage — for a whole container in a single request, **so that** I can prevent accidental over-permissioning in a storage with many resources.

  *Context:* Today a client must traverse the whole resource hierarchy and read every access-control resource to answer 'who can see what?' — the submitting issue names this a standing gap, and a real access-management dashboard (jeswr/solid-access-manager) confirms it: building the by-resource and by-agent grant views requires a full ACL crawl, and distinguishing direct from inherited grants re-implements server-side inheritance logic client-side. The effective-permission summary should be queryable from the server that already computes it.

  *Main flow:*
    1. The owner opens their access-management application.
    2. The application asks the storage, in one request, for the effective grants over a container.
    3. The storage returns each (agent or application, mode, resource-set) grant, marking whether it is direct or inherited.
    4. The owner spots an over-broad inherited grant and revokes it at its source.

  *Derived requirements:* [Authorization Enumeration](#req-authorization-enumeration).

  *Sources:* [#212](https://github.com/w3c/lws-ucs/issues/212), [jeswr/solid-access-manager](https://github.com/jeswr/solid-access-manager)

- **<dfn id="uc-fail-closed-provisioning">Fail-Closed Provisioning of App Data</dfn>** <span class="informative">(`UC-fail-closed-provisioning` — Proposed)</span>

  **As an** application developer, **I want** the containers my app creates to be owner-private from the first instant, with no window in which they are readable more broadly, **so that** a crash, race or misconfiguration during setup can never leave user data exposed.

  *Context:* Every pod-persisting fork in the suite (bookmarks, feeds, social, finance, whiteboards) independently converged on the same hardened provisioning ritual: create the container, write an owner-only access policy FIRST, verify it, only then write data — plus create-only conditions so two concurrent setups cannot half-overwrite each other. The ritual exists because default inherited permissions may be broader than the app's data warrants and policy-write is a separate, failable step. The protocol-level fix is atomic create-with-policy (or default-private-until-policy semantics): make the safe path the only path.

  *Other actors:* user.

  *Error flow:* The app creates its container inside a parent whose inherited policy is public-readable, intending to write a stricter policy next; the app crashes in between. Under create-with-policy (or private-until-policy) semantics this exposure window cannot exist; without them, the user's financial data was public for the duration of the outage.

  *Postconditions:* At no observable instant does the new container's data have broader access than the policy the app requested.

  *Derived requirements:* [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Fail-Closed Creation Semantics](#req-secure-defaults).

  *Sources:* [jeswr/actual](https://github.com/jeswr/actual), [jeswr/linkding](https://github.com/jeswr/linkding), [jeswr/miniflux](https://github.com/jeswr/miniflux)

- **<dfn id="uc-profile-indexing">Indexing a Volunteer Profile</dfn>** <span class="informative">(`UC-profile-indexing` — Proposed)</span>

  **As an** user, **I want** platforms and organisations that offer volunteering opportunities to index my profile, with my consent, **so that** they can reach out to me when opportunities relevant to my profile need volunteers.

  *Context:* Consented third-party indexing of user-controlled data, end to end: the volunteer submits their profile URL and grants read access for the purpose of indexing; indexers are notified of (or poll for) profile updates; suggestions flow back; and the volunteer can both revoke the indexer's access and require removal from the index. Purpose-bound, revocable, notification-driven — a composition of access request, consent, notification and usage-control requirements.

  *Other actors:* service provider.

  *Main flow:*
    1. The volunteer edits their profile and chooses which opportunity providers may access it.
    2. The chosen providers are notified and index the profile for the consented purpose.
    3. The volunteer receives suggestions for matching opportunities, and is notified when new matching opportunities are created.
    4. The volunteer later withdraws one provider's access; that provider must stop indexing and remove the profile from its index.

  *Derived requirements:* [Consent-Based Data Sharing](#req-consent-based-sharing), [Subscribing to Resource Changes (Notifications)](#req-change-notifications), [Usage Control Policies](#req-usage-control).

  *Sources:* [#226](https://github.com/w3c/lws-ucs/issues/226)

- **<dfn id="uc-permission-aware-ui">Permission-Aware User Interface</dfn>** <span class="informative">(`UC-permission-aware-ui` — Proposed)</span>

  **As an** application developer, **I want** to know, when reading a resource, which operations the current user may perform on it, **so that** the UI shows an edit button exactly when editing will succeed — no dead buttons, no trial-and-error writes.

  *Context:* A file-manager UI (jeswr/solid-pod-manager) renders edit/delete/share affordances per resource; an access-management UI (jeswr/solid-access-manager) additionally must not let the user revoke their own control and lock themselves out — both need the server's effective-permission verdict for the CURRENT user on each resource, returned cheaply alongside the read rather than by client-side re-evaluation of the policy graph (which duplicates, and can contradict, the server's logic).

  *Derived requirements:* [Effective-Permission Introspection](#req-permission-introspection).

  *Sources:* [jeswr/solid-access-manager](https://github.com/jeswr/solid-access-manager), [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

- **<dfn id="uc-usage-control">Usage Control</dfn>** <span class="informative">(`UC-usage-control` — Proposed)</span>

  **As a** data owner, **I want** to express usage control conditions in my policies, which go further than mere access control — including the purpose for which a resource may be used, **so that** I can limit what a recipient is allowed to do with my resource after access has taken place, and prevent uses I do not want.

  *Context:* Access control decides who gets in; usage control constrains what happens afterwards. The resource controller must be able to evaluate additional claims about the proposed usage (notably its purpose, #66) and give the recipient a clear, verifiable attestation of the allowed usage; a data protection agency may later audit compliance. Access and usage control are tightly interwoven and need a single policy interface.

  *Other actors:* auditor, collaborator.

  *Preconditions:* Requesting parties can make claims about the purpose of their request. The resource controller can manage policies over resources on an LWS-compatible storage.

  *Main flow:*
    1. The resource controller creates policies specifying for which purposes their resources may be accessed and used.
    2. A requesting party declares the purpose for which the resource will be used when requesting access.
    3. The authorization service compares the requested purpose with the allowed ones and grants or denies access.
    4. The recipient receives a verifiable attestation of the allowed usage, which an auditor can later check.

  *Postconditions:* Policies are enforced consistently across all resources, interfaces and derived views.

  *Derived requirements:* [Usage Control Policies](#req-usage-control).

  *Sources:* [#59](https://github.com/w3c/lws-ucs/issues/59), [#66](https://github.com/w3c/lws-ucs/issues/66)

### Collaboration and communication

- **<dfn id="uc-application-notifications">Application Notifications</dfn>** <span class="informative">(`UC-application-notifications` — Accepted)</span>

  **As an** user, **I want** email or web push notifications for storage activity, **so that** I remain aware of important events.

  *Context:* Notifications keep users engaged with their data.

  *Derived requirements:* [Subscribing to Resource Changes (Notifications)](#req-change-notifications).

  *Sources:* [#100](https://github.com/w3c/lws-ucs/issues/100)

- **<dfn id="uc-meeting-scheduling">Meeting Scheduling</dfn>** <span class="informative">(`UC-meeting-scheduling` — Accepted)</span>

  **As an** user, **I want** to schedule meetings directly through my storage, with conflict detection for online and offline scenarios, **so that** I avoid double-booking.

  *Context:* Integrated scheduling boosts productivity and coordination.

  *Other actors:* collaborator.

  *Derived requirements:* [Inbox (Notifications)](#req-inbox).

  *Sources:* [#3](https://github.com/w3c/lws-ucs/issues/3), [#42](https://github.com/w3c/lws-ucs/issues/42)

- **<dfn id="uc-polling">Polling</dfn>** <span class="informative">(`UC-polling` — Accepted)</span>

  **As an** user, **I want** to create and manage polls within my storage, **so that** I can gather opinions and feedback from others.

  *Context:* Polls support decision-making and community engagement.

  *Derived requirements:* none yet — this use case is not yet covered by a requirement.

  *Sources:* [#144](https://github.com/w3c/lws-ucs/issues/144)

- **<dfn id="uc-real-time-notifications">Real-Time Notifications</dfn>** <span class="informative">(`UC-real-time-notifications` — Accepted)</span>

  **As a** collaborator, **I want** real-time notifications when resources I access are updated, **so that** I stay informed without manual checks.

  *Context:* Timely updates enhance collaboration efficiency.

  *Derived requirements:* [Subscribing to Resource Changes (Notifications)](#req-change-notifications).

  *Sources:* [#32](https://github.com/w3c/lws-ucs/issues/32), [#79](https://github.com/w3c/lws-ucs/issues/79)

- **<dfn id="uc-semantic-collaboration">Semantic Collaboration</dfn>** <span class="informative">(`UC-semantic-collaboration` — Accepted)</span>

  **As an** user, **I want** to co-author structured content with others using permanent URIs and flexible permissions, **so that** collaboration is efficient and traceable.

  *Context:* This enables advanced use cases like shared knowledge bases.

  *Other actors:* collaborator.

  *Derived requirements:* [Collaborative Editing](#req-collaborative-editing).

  *Sources:* [#98](https://github.com/w3c/lws-ucs/issues/98), [#146](https://github.com/w3c/lws-ucs/issues/146)

- **<dfn id="uc-universal-communication">Universal Communication</dfn>** <span class="informative">(`UC-universal-communication` — Accepted)</span>

  **As an** user, **I want** direct messaging channels with other storage owners, **so that** I can collaborate seamlessly within the platform.

  *Context:* Built-in communication strengthens user interaction.

  *Derived requirements:* [Inbox (Notifications)](#req-inbox).

  *Sources:* [#22](https://github.com/w3c/lws-ucs/issues/22), [#99](https://github.com/w3c/lws-ucs/issues/99)

- **<dfn id="uc-federated-task-dashboard">Federated Task Dashboard</dfn>** <span class="informative">(`UC-federated-task-dashboard` — Proposed)</span>

  **As an** user, **I want** to see every task assigned to me in one view, across all the project storages I collaborate in, **so that** work assigned to me in ten different pods behaves like one work queue.

  *Context:* An issue tracker whose issues live in project pods (jeswr/solid-issues over the shared jeswr/solid-task-model) plus a dashboard aggregating 'assigned to me' (Pod Manager) require: a shared task vocabulary, access-control-respecting reads across many storages, and change notifications so the dashboard stays current without polling every project pod. This is the concrete everyday shape of the federated-query requirement.

  *Other actors:* collaborator.

  *Derived requirements:* [Data Location Registry](#req-app-data-registry), [Federated Data Queries](#req-federated-queries), [Subscribing to Resource Changes (Notifications)](#req-change-notifications).

  *Sources:* [jeswr/solid-issues](https://github.com/jeswr/solid-issues), [jeswr/solid-task-model](https://github.com/jeswr/solid-task-model)

### Application integration

- **<dfn id="uc-byod-apps">'Bring Your Own Data' Apps</dfn>** <span class="informative">(`UC-byod-apps` — Accepted)</span>

  **As an** application developer, **I want** my applications to store data in the user's storage, with support for CRUD operations and store discovery, **so that** users retain ownership and control of their data.

  *Context:* This shifts data ownership from apps to users.

  *Other actors:* user.

  *Derived requirements:* [Self-Descriptive and Discoverable APIs](#req-self-descriptive-apis).

  *Sources:* [#12](https://github.com/w3c/lws-ucs/issues/12), [#120](https://github.com/w3c/lws-ucs/issues/120)

- **<dfn id="uc-business-data-access">Business Data Access</dfn>** <span class="informative">(`UC-business-data-access` — Accepted)</span>

  **As a** data owner, **I want** clear enforcement rules for data sharing, **so that** enterprise integrations comply with organizational policies.

  *Context:* A business user needs enterprise data sharing (granting and requesting access to business data) to comply with organizational policy — secure enterprise use cases.

  *Derived requirements:* [Access Request Handling](#req-access-request-handling).

  *Sources:* [#27](https://github.com/w3c/lws-ucs/issues/27), [#28](https://github.com/w3c/lws-ucs/issues/28)

- **<dfn id="uc-data-integration">Data Integration</dfn>** <span class="informative">(`UC-data-integration` — Accepted)</span>

  **As an** application developer, **I want** a standardized API to combine data from multiple sources, **so that** integrating diverse datasets is straightforward and efficient.

  *Context:* Simplified integration reduces development complexity.

  *Derived requirements:* [Federated Data Queries](#req-federated-queries), [Federated Query Joins](#req-federated-query-joins), [Serialization Format](#req-serialization-format).

  *Sources:* [#26](https://github.com/w3c/lws-ucs/issues/26), [#53](https://github.com/w3c/lws-ucs/issues/53), [#88](https://github.com/w3c/lws-ucs/issues/88), [#106](https://github.com/w3c/lws-ucs/issues/106)

- **<dfn id="uc-digital-goods-delivery">Digital Goods Delivery</dfn>** <span class="informative">(`UC-digital-goods-delivery` — Accepted)</span>

  **As an** user, **I want** secure delivery of digital goods (e.g., software, media) with confirmation receipts, **so that** providers can deliver assets with minimal intervention.

  *Context:* This ensures reliable digital product delivery.

  *Other actors:* service provider.

  *Derived requirements:* [Auditable Trail](#req-auditable-trail).

  *Sources:* [#14](https://github.com/w3c/lws-ucs/issues/14)

- **<dfn id="uc-personal-information-management">Personal Information Management</dfn>** <span class="informative">(`UC-personal-information-management` — Accepted)</span>

  **As an** user, **I want** to manage my personal data in my storage and integrate it with non-LWS apps via some data transformation, **so that** I can use various apps without creating data silos.

  *Context:* This promotes interoperability and user control.

  *Derived requirements:* [Personal Data Projection](#req-personal-data-projection), [Serialization Format](#req-serialization-format).

  *Sources:* [#2](https://github.com/w3c/lws-ucs/issues/2)

- **<dfn id="uc-ai-agent-access">AI Agent Access to Storage</dfn>** <span class="informative">(`UC-ai-agent-access` — Proposed)</span>

  **As an** user, **I want** to let an AI assistant read (and, where I say so, write) selected parts of my storage, **so that** my assistant works over my actual data while everything it does stays bounded and attributable to it — not to me.

  *Context:* A protocol server exposing a pod to AI agents (jeswr/solid-mcp) ships read-only by default, with a fail-closed scope guard and per-hop redirect protection — all client-side, because the storage offers no way to issue an agent a credential that the STORAGE enforces as read-only-within-subtree. Agent access sharpens three needs: least-privilege scoping enforced server-side, audit attribution distinguishing the agent from the delegating user (the administrative-assistant requirement, mechanised), and revocation that kills the agent's authority instantly.

  *Other actors:* autonomous agent.

  *Error flow:* The agent, misled by a prompt-injected instruction, attempts to read outside its granted subtree and then to exfiltrate via a redirect to a foreign host. The storage-enforced scope rejects the out-of-scope read regardless of what the agent's client-side guard does, and the attempt is attributed to the agent in the audit trail.

  *Derived requirements:* [Attribution of Writes](#req-write-attribution), [Auditable Trail](#req-auditable-trail), [Least-Privilege Scoped Credentials](#req-scoped-access).

  *Sources:* [jeswr/solid-mcp](https://github.com/jeswr/solid-mcp)

- **<dfn id="uc-public-index-crawl">Crawling and Indexing Public Storage Data</dfn>** <span class="informative">(`UC-public-index-crawl` — Proposed)</span>

  **As a** service provider, **I want** to crawl and index publicly readable profiles and documents across storages, honouring each owner's indexing preferences, and to accept owner-initiated suggestions, **so that** people and data become findable across the decentralised web without a central platform.

  *Context:* A WebID search platform (jeswr/solid-webid-index) crawls public profiles and lets owners push their own profile via an inbox notification for immediate (re)indexing. From the storage side this needs: clear public-readability semantics, machine-readable indexing consent (may this be indexed? — the selective-indexing declaration, outward-facing), an inbox to receive index-me suggestions, and polite-crawl affordances (rate-limit signalling, cheap conditional revalidation of unchanged profiles).

  *Other actors:* user.

  *Derived requirements:* [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Inbox (Notifications)](#req-inbox), [Indexing Control](#req-indexing-control), [Rate-Limit Signaling](#req-rate-limit-signaling).

  *Sources:* [jeswr/solid-webid-index](https://github.com/jeswr/solid-webid-index)

- **<dfn id="uc-cross-app-interop">Cross-Application Data Interoperability</dfn>** <span class="informative">(`UC-cross-app-interop` — Proposed)</span>

  **As an** application developer, **I want** data written by one application to be readable and safely writable by every other application the user chooses, **so that** the user's chat history (or tasks, or bookmarks) is one corpus, not one silo per app.

  *Context:* Reconciling chat messages across three incompatible app conventions into one canonical model (jeswr/solid-chat-interop, covering ActivityStreams 2.0, SolidOS LongChat and LibreChat) surfaced what interop actually takes: agreed vocabularies and shapes, defensive reading (a malformed literal written by one app must drop a field, not abort every other app's parse), asymmetric conventions (exactly one canonical reply edge, not two inverse ones), and attribution of which app wrote what. The storage protocol's contribution is the conventions registry: a discoverable, shared statement of where data of a given shape lives and which shapes apply (cf. the non-owner app choice of issue #120).

  *Other actors:* user.

  *Derived requirements:* [Attribution of Writes](#req-write-attribution), [Data Location Registry](#req-app-data-registry), [Serialization Format](#req-serialization-format).

  *Sources:* [#120](https://github.com/w3c/lws-ucs/issues/120), [jeswr/solid-chat-interop](https://github.com/jeswr/solid-chat-interop)

- **<dfn id="uc-app-data-discovery">Discovering Where Data Lives</dfn>** <span class="informative">(`UC-app-data-discovery` — Proposed)</span>

  **As an** application developer, **I want** to find where in a user's storage the data of a given class lives (their contacts, their tasks, their bookmarks), and to register where my app put its data, **so that** a newly authorized app finds existing data instead of starting an empty parallel world.

  *Context:* The general-purpose manager (jeswr/solid-pod-manager) must locate every data class any app has stored; each suite app must register its containers so others (and the manager) find them — the type-index pattern. It must be authorized-only and non-leaky (an app allowed to see bookmarks must not learn that health data exists — issue #222), and needs bootstrap semantics: what happens when no registry exists yet.

  *Preconditions:* The app is authorized for the data class it queries the registry for.

  *Derived requirements:* [Data Location Registry](#req-app-data-registry), [Non-Leaky Discovery](#req-non-leaky-discovery).

  *Sources:* [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

- **<dfn id="uc-selective-indexing">Indexed and Non-Indexed Data</dfn>** <span class="informative">(`UC-selective-indexing` — Proposed)</span>

  **As an** application developer, **I want** to mark part of my app's data as indexable (e.g. through a type index or search index) and other parts as not indexable, **so that** indexers surface the meaningful data and are not spoofed with internal representations (e.g. CRDT history) that are useless outside their specific structure.

  *Context:* Not all stored data is meaningful to other consumers: sync logs, CRDT update histories and caches are only useful in their specific form. An indexer (server- or client-side) must be able to distinguish data worth surfacing from internal structure — whether the marking lives on the data, the container, storage configuration, or type hierarchy is a design choice for the protocol.

  *Derived requirements:* [Indexing Control](#req-indexing-control).

  *Sources:* [#208](https://github.com/w3c/lws-ucs/issues/208)

- **<dfn id="uc-legacy-app-migration">Migrating an Existing App onto User Storage</dfn>** <span class="informative">(`UC-legacy-app-migration` — Proposed)</span>

  **As an** application developer, **I want** to replace an existing app's private database with user-controlled storage while keeping the app's UX intact, **so that** the fastest route to adoption: users keep the app they like and gain ownership of its data.

  *Context:* Three production OSS apps were forked to pod persistence (jeswr/linkding bookmarks, jeswr/miniflux feed reading, jeswr/elk social): the browser app keeps its interface and swaps the persistence layer. What the migrations consistently needed from storage: full browser access from a foreign web origin (the app is not served by the storage provider), a stable application identity users can recognize at consent (per deployment origin), safe-by-default provisioning of the app's containers, and known serializations. Server-side components (the feed fetcher) additionally need the non-interactive service authentication the backend-integration story already covers.

  *Derived requirements:* [Browser Access from Foreign Origins](#req-cors-browser-access), [Fail-Closed Creation Semantics](#req-secure-defaults), [Serialization Format](#req-serialization-format), [Stable, Verifiable Application Identity](#req-app-identity).

  *Sources:* [jeswr/elk](https://github.com/jeswr/elk), [jeswr/linkding](https://github.com/jeswr/linkding), [jeswr/miniflux](https://github.com/jeswr/miniflux)

- **<dfn id="uc-agent-memory">User-Owned Agent Memory</dfn>** <span class="informative">(`UC-agent-memory` — Proposed)</span>

  **As an** user, **I want** AI agents to keep their memory about me in MY storage rather than in each vendor's silo, **so that** memory becomes portable across agents and vendors, inspectable, and deletable by me.

  *Context:* An agent-memory backend over pods (jeswr/solid-memory with an adapter for an agent framework, jeswr/openclaw-memory-solid): memory items are typed RDF, owner-private by default, carrying provenance of which agent generated each item. The storage needs are least-privilege agent credentials (an agent reads/writes only its memory container), provenance attribution per write, and the user's unilateral right to inspect and delete — which falls out of ordinary resource control once memory is IN the storage.

  *Other actors:* autonomous agent.

  *Derived requirements:* [Attribution of Writes](#req-write-attribution), [Least-Privilege Scoped Credentials](#req-scoped-access).

  *Sources:* [jeswr/openclaw-memory-solid](https://github.com/jeswr/openclaw-memory-solid), [jeswr/solid-memory](https://github.com/jeswr/solid-memory)

- **<dfn id="uc-workflow-automation">Workflow Automation over Storage</dfn>** <span class="informative">(`UC-workflow-automation` — Proposed)</span>

  **As an** user, **I want** my automation workflows (low-code pipelines, scheduled jobs) to read and write my storage as one step among many, **so that** my storage participates in the automation ecosystem — a new bookmark can trigger a pipeline; a pipeline can file data into my pod.

  *Context:* A community node for a workflow platform (jeswr/n8n-nodes-solid) exposes storage CRUD to non-technical automation builders. Its hard requirements from the storage: credentials grantable to a WORKFLOW, scoped to a container subtree (the pipeline must not hold the user's full authority — the node enforces a pod-scope guard client-side today, which the server cannot verify); machine-actionable errors (a pipeline branches on 'conflict' vs 'forbidden' vs 'rate-limited'); and explicit rate-limit signalling with retry timing, since a fan-out pipeline hammers the storage in bursts.

  *Other actors:* autonomous agent.

  *Derived requirements:* [Least-Privilege Scoped Credentials](#req-scoped-access), [Rate-Limit Signaling](#req-rate-limit-signaling), [Server-to-Server Authentication](#req-server-to-server-auth), [Structured, Machine-Actionable Errors](#req-structured-errors).

  *Sources:* [jeswr/n8n-nodes-solid](https://github.com/jeswr/n8n-nodes-solid)

### Advanced features

- **<dfn id="uc-contextual-interactions">Contextual Interactions</dfn>** <span class="informative">(`UC-contextual-interactions` — Accepted)</span>

  **As an** user, **I want** context-aware display of interactions alongside content, **so that** I can understand permissions and history intuitively.

  *Context:* This improves user understanding of data interactions.

  *Derived requirements:* none yet — this use case is not yet covered by a requirement.

  *Sources:* [#55](https://github.com/w3c/lws-ucs/issues/55)

- **<dfn id="uc-home-access">Home Access</dfn>** <span class="informative">(`UC-home-access` — Accepted)</span>

  **As an** user, **I want** to access my storage from home devices with dynamic IPs, **so that** connectivity issues don't prevent me from using my data.

  *Context:* This ensures accessibility in home environments (self-hosting on home desktops or NAS devices behind consumer connections).

  *Derived requirements:* none yet — this use case is not yet covered by a requirement.

  *Sources:* [#68](https://github.com/w3c/lws-ucs/issues/68), [#105](https://github.com/w3c/lws-ucs/issues/105)

- **<dfn id="uc-legal-reporting">Legal Reporting</dfn>** <span class="informative">(`UC-legal-reporting` — Accepted)</span>

  **As a** data owner, **I want** verifiable proof of data sharing to support audit compliance, **so that** I can meet legal obligations even after access is revoked.

  *Context:* This ensures transparency and accountability.

  *Other actors:* auditor.

  *Derived requirements:* [Auditable Trail](#req-auditable-trail), [Data Integrity Verification](#req-data-integrity-verification).

  *Sources:* [#9](https://github.com/w3c/lws-ucs/issues/9)

- **<dfn id="uc-pagination-filtering">Pagination & Filtering</dfn>** <span class="informative">(`UC-pagination-filtering` — Accepted)</span>

  **As an** user, **I want** efficient pagination, filtering, and ordering of search results, **so that** I can navigate large datasets easily.

  *Context:* These features enhance data usability.

  *Derived requirements:* [Pagination, Filtering and Sorting](#req-paginate-filter-sort), [Search and Query](#req-search-and-query).

  *Sources:* [#103](https://github.com/w3c/lws-ucs/issues/103)

- **<dfn id="uc-search-functionality">Search Functionality</dfn>** <span class="informative">(`UC-search-functionality` — Accepted)</span>

  **As an** user, **I want** powerful search capabilities with contextual awareness and security enforcement, **so that** I can find relevant resources quickly and safely.

  *Context:* Effective search is essential for large datasets.

  *Derived requirements:* [Metadata Query](#req-metadata-query), [Pagination, Filtering and Sorting](#req-paginate-filter-sort), [Pod-Level Query](#req-pod-level-query), [Query Other Storages](#req-query-other-pods), [Resource-Level Query](#req-resource-level-query), [Search and Query](#req-search-and-query).

  *Sources:* [#87](https://github.com/w3c/lws-ucs/issues/87), [#152](https://github.com/w3c/lws-ucs/issues/152)

- **<dfn id="uc-sensor-data-sharing">Sensor Data Sharing</dfn>** <span class="informative">(`UC-sensor-data-sharing` — Accepted)</span>

  **As an** user, **I want** to share sensor data at varying levels of granularity without duplication, **so that** consumers receive only the detail they need.

  *Context:* Efficient sharing reduces resource usage.

  *Derived requirements:* [View-Based Data Sharing](#req-view-based-sharing).

  *Sources:* [#8](https://github.com/w3c/lws-ucs/issues/8)

- **<dfn id="uc-sparql-queries">SPARQL Queries</dfn>** <span class="informative">(`UC-sparql-queries` — Accepted)</span>

  **As an** user, **I want** support for SPARQL queries to perform complex searches and data analysis, **so that** I can extract insights from linked data.

  *Context:* A power user's story: SPARQL enables advanced semantic web queries.

  *Derived requirements:* [Federated Data Queries](#req-federated-queries), [Federated Query Joins](#req-federated-query-joins), [Pagination, Filtering and Sorting](#req-paginate-filter-sort), [Pod-Level Query](#req-pod-level-query), [Query Other Storages](#req-query-other-pods), [Resource-Level Query](#req-resource-level-query), [Search and Query](#req-search-and-query).

  *Sources:* [#45](https://github.com/w3c/lws-ucs/issues/45)

- **<dfn id="uc-storage-listening">Storage Listening</dfn>** <span class="informative">(`UC-storage-listening` — Accepted)</span>

  **As an** application developer, **I want** offline monitoring of storage changes, **so that** my applications stay synchronized even without connectivity.

  *Context:* This supports robust offline app functionality: an application that was offline can catch up on what changed while it was away.

  *Derived requirements:* [Offline Access and Synchronization](#req-offline-sync).

  *Sources:* [#101](https://github.com/w3c/lws-ucs/issues/101)

- **<dfn id="uc-timeseries-storage">Timeseries Storage</dfn>** <span class="informative">(`UC-timeseries-storage` — Accepted)</span>

  **As an** user, **I want** to store timeseries data with resolution limits and multidimensional analysis support, **so that** I can efficiently analyze trends over time.

  *Context:* This is critical for applications like IoT or analytics.

  *Derived requirements:* [Timeseries Data Support](#req-timeseries).

  *Sources:* [#6](https://github.com/w3c/lws-ucs/issues/6)

- **<dfn id="uc-webid-profile-interaction">WebID Profile Interaction</dfn>** <span class="informative">(`UC-webid-profile-interaction` — Accepted)</span>

  **As an** user, **I want** clicking a WebID to display profiles and available actions, **so that** I can engage with contacts effortlessly.

  *Context:* This enhances social and professional interactions.

  *Derived requirements:* [Profile Interaction UI](#req-profile-interaction-ui).

  *Sources:* [#47](https://github.com/w3c/lws-ucs/issues/47), [#48](https://github.com/w3c/lws-ucs/issues/48)

- **<dfn id="uc-website-creation">Website Creation</dfn>** <span class="informative">(`UC-website-creation` — Accepted)</span>

  **As an** user, **I want** to publish self-describing websites with persistent URIs, **so that** my content remains accessible and interoperable over time.

  *Context:* This supports durable web publishing.

  *Derived requirements:* [Self-Describing Website Publication](#req-website-publication).

  *Sources:* [#31](https://github.com/w3c/lws-ucs/issues/31)

## Non-Functional Stories

### Security and privacy

- **<dfn id="uc-e2e-encryption">'End to End' Encryption</dfn>** <span class="informative">(`UC-e2e-encryption` — Accepted)</span>

  **As an** user, **I want** end-to-end encryption for all data storage and transfers, **so that** only authorized parties can decrypt and access my information.

  *Context:* Encryption ensures data confidentiality — even against the storage provider itself.

  *Derived requirements:* [End-to-End Encryption](#req-e2e-encryption).

  *Sources:* [#4](https://github.com/w3c/lws-ucs/issues/4), [#44](https://github.com/w3c/lws-ucs/issues/44), [#73](https://github.com/w3c/lws-ucs/issues/73), [#74](https://github.com/w3c/lws-ucs/issues/74), [#75](https://github.com/w3c/lws-ucs/issues/75), [#76](https://github.com/w3c/lws-ucs/issues/76)

- **<dfn id="uc-consent-based-sharing">Consent-Based Sharing</dfn>** <span class="informative">(`UC-consent-based-sharing` — Accepted)</span>

  **As an** user, **I want** verifiable consent mechanisms with audit trails for data sharing, **so that** I can ensure compliance with privacy regulations.

  *Context:* Consent management supports ethical data practices. The cluster of usage-control issues (#80–#86) elaborates purpose-based, processing-based and automated usage control on top of consent.

  *Derived requirements:* [Consent-Based Data Sharing](#req-consent-based-sharing), [Usage Control Policies](#req-usage-control).

  *Sources:* [#80](https://github.com/w3c/lws-ucs/issues/80), [#81](https://github.com/w3c/lws-ucs/issues/81), [#82](https://github.com/w3c/lws-ucs/issues/82), [#83](https://github.com/w3c/lws-ucs/issues/83), [#84](https://github.com/w3c/lws-ucs/issues/84), [#85](https://github.com/w3c/lws-ucs/issues/85), [#86](https://github.com/w3c/lws-ucs/issues/86), [#141](https://github.com/w3c/lws-ucs/issues/141)

- **<dfn id="uc-legal-grounds-support">Legal Grounds Support</dfn>** <span class="informative">(`UC-legal-grounds-support` — Accepted)</span>

  **As a** compliance officer, **I want** to define access policies based on legal grounds (e.g., GDPR), **so that** data sharing adheres to regulatory requirements.

  *Context:* This ensures global compliance readiness. Issue #210 extends it to differing legal CONTEXTS: the applicable local, state or national law of the user and of the storage may differ, and policies must be definable against the established legal context.

  *Alternative flow:* A compliance officer checks access controls for adherence to local law: the same sharing policy evaluates differently under the storage's jurisdiction than under the user's, and the policy engine resolves which legal context governs (from issue #210).

  *Derived requirements:* [Legal Basis Enforcement](#req-legal-basis-enforcement).

  *Sources:* [#77](https://github.com/w3c/lws-ucs/issues/77), [#80](https://github.com/w3c/lws-ucs/issues/80), [#141](https://github.com/w3c/lws-ucs/issues/141), [#210](https://github.com/w3c/lws-ucs/issues/210)

- **<dfn id="uc-mutation-validation">Custom Validation of Mutating Requests</dfn>** <span class="informative">(`UC-mutation-validation` — Proposed)</span>

  **As a** data owner, **I want** to specify validation rules for requests that mutate a resource, **so that** the storage enforces those rules, securing the resource against invalid data and spam.

  *Context:* Append/write permission alone is too blunt for social resources: a group members list should accept only well-shaped membership triples about the authenticated agent themself; an inbox should accept only valid notifications whose actor matches the sender. Without server-side validation, any agent with append access can dump arbitrary data.

  *Other actors:* application developer.

  *Main flow:*
    1. The owner attaches a validation rule to a group resource: only membership triples whose subject is the group and whose object is the authenticated agent's identifier may be added or removed.
    2. A member appends themself to the group; the mutation validates and is applied.
    3. An application posts a notification to the owner's inbox; the notification validates against the inbox's accepted shape and is stored.

  *Error flow:* A malicious agent attempts to append somebody else to the group, or to spoof a notification naming another actor; the storage rejects the mutation with a structured validation error.

  *Derived requirements:* [Server-Side Write Validation](#req-write-validation).

  *Sources:* [#93](https://github.com/w3c/lws-ucs/issues/93)

- **<dfn id="uc-private-data-discovery">Privacy in Data Discovery</dfn>** <span class="informative">(`UC-private-data-discovery` — Proposed)</span>

  **As an** user, **I want** data discovery to respect my privacy, **so that** unauthorized parties can't profile me because my storage discloses too much through the discovery layer itself.

  *Context:* Discovery is itself a disclosure channel: when a tax app asks where tax-relevant data lives, the storage must not reveal to it that health-related data classes exist (their mere existence can suggest, e.g., a pregnancy). Authorized discovery must return exactly the authorized data locations and nothing about the existence of anything else.

  *Other actors:* application developer.

  *Error flow:* Jane authorizes the tax app to discover tax-relevant data only; during discovery one of her storages nonetheless discloses the existence of health-related data types to the tax app. This is the failure the requirement forbids.

  *Derived requirements:* [Non-Leaky Discovery](#req-non-leaky-discovery).

  *Sources:* [#222](https://github.com/w3c/lws-ucs/issues/222)

- **<dfn id="uc-pseudonymous-access">Pseudonymous Access for Vendors</dfn>** <span class="informative">(`UC-pseudonymous-access` — Proposed)</span>

  **As an** user, **I want** vendors to access my data without being able to uniquely identify me across services, **so that** vendors cannot track me across domains or correlate their records with other vendors'.

  *Context:* Fixed identifier or storage URLs (https://ID.provider.example, /ID/ paths) let vendors track a user across vendor domains or collude by exchanging the stable identifier. The storage/identity layer needs rotating per-vendor aliases (pseudo-identifiers) — per vendor, and rotatable over time for a single vendor.

  *Other actors:* service provider.

  *Derived requirements:* [Pseudonymous Identifiers](#req-pseudonymity).

  *Sources:* [#195](https://github.com/w3c/lws-ucs/issues/195)

### Performance and usability

- **<dfn id="uc-clear-error-messages">Clear Error Messages</dfn>** <span class="informative">(`UC-clear-error-messages` — Accepted)</span>

  **As an** user, **I want** error messages that are clear and actionable, **so that** I can resolve issues quickly and without frustration.

  *Context:* Good error handling enhances user experience. For applications this means machine-readable error structure, not just human-readable text — an application can only render an actionable message if the server tells it precisely what failed.

  *Other actors:* application developer.

  *Derived requirements:* [Structured, Machine-Actionable Errors](#req-structured-errors).

  *Sources:* [#34](https://github.com/w3c/lws-ucs/issues/34)

- **<dfn id="uc-performant-access-control">Performant Access Control</dfn>** <span class="informative">(`UC-performant-access-control` — Accepted)</span>

  **As an** user, **I want** access control mechanisms that are responsive and scalable, **so that** the system performs well even under heavy load.

  *Context:* Performance is critical for large-scale use.

  *Derived requirements:* [Performance and Scalability](#req-performance-scalability).

  *Sources:* [#71](https://github.com/w3c/lws-ucs/issues/71), [#72](https://github.com/w3c/lws-ucs/issues/72), [#153](https://github.com/w3c/lws-ucs/issues/153)

- **<dfn id="uc-storage-ownership">Storage Ownership</dfn>** <span class="informative">(`UC-storage-ownership` — Accepted)</span>

  **As an** user, **I want** ownership assigned upon storage creation, **so that** I have full control from the outset.

  *Context:* Immediate ownership clarifies user authority. The relationship between the controller of a storage and the controller of a resource within it is under WG clarification (issue #213).

  *Derived requirements:* [Control of Storages](#req-control-of-storages).

  *Sources:* [#43](https://github.com/w3c/lws-ucs/issues/43), [#213](https://github.com/w3c/lws-ucs/issues/213)

## Technical Stories

### Identity, authentication and trust

- **<dfn id="uc-authentication-mechanisms">Authentication Mechanism(s)</dfn>** <span class="informative">(`UC-authentication-mechanisms` — Accepted)</span>

  **As an** user, **I want** support for modern authentication methods like passkeys, silent authentication, and script-friendly options, **so that** I can authenticate securely across diverse scenarios.

  *Context:* Flexible authentication meets varied user needs: passkey/WebAuthn login (#51), browser-level login (#50), logging back into applications without re-directing to the identity provider (#49), silent authentication (#41), and script/backend-friendly flows.

  *Derived requirements:* [Authentication Mechanisms](#req-authentication-mechanisms), [Silent Session Continuation](#req-silent-reauth).

  *Sources:* [#39](https://github.com/w3c/lws-ucs/issues/39), [#41](https://github.com/w3c/lws-ucs/issues/41), [#49](https://github.com/w3c/lws-ucs/issues/49), [#50](https://github.com/w3c/lws-ucs/issues/50), [#51](https://github.com/w3c/lws-ucs/issues/51), [#114](https://github.com/w3c/lws-ucs/issues/114), [#129](https://github.com/w3c/lws-ucs/issues/129), [#130](https://github.com/w3c/lws-ucs/issues/130), [#136](https://github.com/w3c/lws-ucs/issues/136), [#162](https://github.com/w3c/lws-ucs/issues/162)

- **<dfn id="uc-globally-unique-identifiers">Globally Unique Identity</dfn>** <span class="informative">(`UC-globally-unique-identifiers` — Accepted)</span>

  **As an** user, **I want** my identity, my storages, and the resources in them to be identified by globally unique identifiers, **so that** anything I control can be referenced unambiguously from anywhere, by anyone I choose, without central coordination.

  *Context:* RECONSTRUCTED: the requirements document back-referenced a story named 'Globally Unique Identifiers' that did not exist in the stories list — a dangling by-name reference now caught by the machine-checked motivatedBy chain. The submitted [UC] issues (#115 entity identity, #108 storage identity) supply the content: entities and storages need global, collision-free identity for cross-storage reference, access control and portability.

  *Derived requirements:* [Globally Unique Identifiers](#req-globally-unique-identifiers).

  *Sources:* [#108](https://github.com/w3c/lws-ucs/issues/108), [#115](https://github.com/w3c/lws-ucs/issues/115), [#136](https://github.com/w3c/lws-ucs/issues/136)

- **<dfn id="uc-identity-credentials-management">Identity & Credentials Management</dfn>** <span class="informative">(`UC-identity-credentials-management` — Accepted)</span>

  **As an** user, **I want** to manage my identities and credentials locally, **so that** I control my authentication process directly from my device.

  *Context:* Local management boosts security and autonomy.

  *Derived requirements:* [Authentication Mechanisms](#req-authentication-mechanisms).

  *Sources:* [#25](https://github.com/w3c/lws-ucs/issues/25), [#90](https://github.com/w3c/lws-ucs/issues/90), [#115](https://github.com/w3c/lws-ucs/issues/115), [#128](https://github.com/w3c/lws-ucs/issues/128), [#153](https://github.com/w3c/lws-ucs/issues/153)

- **<dfn id="uc-storage-provider-trust">Trust Mechanism for Storage Providers</dfn>** <span class="informative">(`UC-storage-provider-trust` — Accepted)</span>

  **As a** storage provider, **I want** a mechanism to trust Identity Providers for authenticating entities, **so that** I can ensure only authenticated and authorized entities access the storage.

  *Context:* This trust relationship is crucial for maintaining security in a decentralized system where multiple Identity Providers may be involved.

  *Derived requirements:* [Trusted Identity Providers](#req-trusted-identity-providers), [Use of Service Providers](#req-service-providers).

  *Sources:* [#129](https://github.com/w3c/lws-ucs/issues/129)

- **<dfn id="uc-id-alias">ID Alias</dfn>** <span class="informative">(`UC-id-alias` — Proposed)</span>

  **As an** user, **I want** to link multiple identifiers as aliases of the same entity, **so that** any of my identifiers represents me — access keeps working when one identity service is down, and unlinking one alias never breaks social links held under the others.

  *Context:* Alias semantics beyond migration: grants made to one identifier honour requests presented under its aliases; aliases are individually revocable (removing one revokes only that identifier's access); and contacts can address the entity under any active alias. Error handling matters: the home server of one alias being unreachable must not lock out access under another.

  *Main flow:*
    1. Alice declares identifiers ID-B and ID-C as aliases of her identifier ID-A.
    2. A resource granted to ID-A accepts requests authenticated as ID-B or ID-C.
    3. Alice retires ID-B; resources stop accepting ID-B while ID-A and ID-C continue to work.
    4. Alice's contacts can reach her under any active alias; retiring one alias breaks no social link held under the others.

  *Derived requirements:* [Globally Unique Identifiers](#req-globally-unique-identifiers).

  *Sources:* [#211](https://github.com/w3c/lws-ucs/issues/211)

- **<dfn id="uc-recognizable-app-identity">Recognizable Application Identity</dfn>** <span class="informative">(`UC-recognizable-app-identity` — Proposed)</span>

  **As an** user, **I want** the consent screen to name the actual application I am authorizing — stably across sessions and deployments, **so that** I can make a meaningful trust decision, recognise the app in my grant list later, and revoke exactly it.

  *Context:* With throwaway dynamic client registration the consent screen shows a random opaque identifier; the user learns nothing and the grant list is unreviewable. Every deployed suite app moved to a stable application identifier document (name, logo, redirect URIs) served by the app — with the operational gotcha that the identity is per deployment ORIGIN (a Vercel preview and production are different apps to the authorization server). Grants keyed to the stable app identity are what make the access-overview dashboard's by-application view possible.

  *Other actors:* application developer.

  *Derived requirements:* [Stable, Verifiable Application Identity](#req-app-identity).

  *Sources:* [jeswr/linkding](https://github.com/jeswr/linkding), [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)

- **<dfn id="uc-silent-session-restore">Silent Session Restore</dfn>** <span class="informative">(`UC-silent-session-restore` — Proposed)</span>

  **As an** user, **I want** reopening an app to silently restore my authenticated session — no redirect, no popup, no re-login — until I log out or the grant is revoked, **so that** apps over my storage feel like apps, not like a login treadmill.

  *Context:* The single most re-implemented piece of client plumbing in the suite (extracted to jeswr/solid-session-restore after being hand-rolled per app, then hardened again in the Elk and Excalidraw forks): persist a scoped refresh credential per user, restore the session by a silent token refresh on load, guard against restoring another user's session on a shared device (cross-user generation guard), and fall back to interactive login only on genuine failure. The protocol-level need: an auth flow with a persistable, silently refreshable, individually revocable credential — with sensitive-operation step-up (the passkey re-authentication profile) composing on top.

  *Other actors:* application developer.

  *Main flow:*
    1. The user logs into the app once; the app persists a scoped refresh credential bound to that user.
    2. Days later the user reopens the app; it silently refreshes the session and lands on the actual page, showing only a brief restoring state.
    3. The user revokes the app's grant from another device; the next refresh fails cleanly and the app returns to login.
    4. On a shared device, a different user's login evicts the stored credential rather than restoring the wrong identity.

  *Derived requirements:* [Silent Session Continuation](#req-silent-reauth).

  *Sources:* [jeswr/elk](https://github.com/jeswr/elk), [jeswr/solid-session-restore](https://github.com/jeswr/solid-session-restore)

### API and protocol flexibility

- **<dfn id="uc-api-protocol-decoupling">API Protocol Decoupling</dfn>** <span class="informative">(`UC-api-protocol-decoupling` — Accepted)</span>

  **As an** application developer, **I want** APIs decoupled from HTTP, **so that** I can build local-first applications or use alternative protocols like gRPC or GraphQL.

  *Context:* Decoupling enhances development flexibility.

  *Derived requirements:* [Loose Coupling of Underlying Protocols](#req-protocol-decoupling).

  *Sources:* [#24](https://github.com/w3c/lws-ucs/issues/24)

- **<dfn id="uc-backend-service-integration">Backend Service Integration</dfn>** <span class="informative">(`UC-backend-service-integration` — Accepted)</span>

  **As a** service provider, **I want** secure authentication methods like mTLS or simpler alternatives for backend services, **so that** integration with LWS is seamless and secure.

  *Context:* This ensures reliable backend connectivity.

  *Derived requirements:* [Server-to-Server Authentication](#req-server-to-server-auth).

  *Sources:* [#40](https://github.com/w3c/lws-ucs/issues/40), [#56](https://github.com/w3c/lws-ucs/issues/56), [#92](https://github.com/w3c/lws-ucs/issues/92)

- **<dfn id="uc-storage-description-discovery">Storage Description and Discovery</dfn>** <span class="informative">(`UC-storage-description-discovery` — Accepted)</span>

  **As an** application developer, **I want** to retrieve metadata about available storage and service capabilities, **so that** I can configure interactions appropriately and adapt to different storage behaviors.

  *Context:* Describing server capabilities in a standardized way allows clients to dynamically adjust their operations, improves interoperability, and facilitates tooling or automation.

  *Other actors:* user.

  *Derived requirements:* [Self-Descriptive and Discoverable APIs](#req-self-descriptive-apis).

  *Sources:* [#21](https://github.com/w3c/lws-ucs/issues/21)

- **<dfn id="uc-custom-api-endpoints">User-Defined Custom API Endpoints</dfn>** <span class="informative">(`UC-custom-api-endpoints` — Proposed)</span>

  **As a** data owner, **I want** to attach custom API endpoints to my storage that are served by third-party services of my choosing, **so that** my storage supports additional functionality (virtual resources, extra policy engines, delegated computation, protocol bridges) without requiring the storage provider to implement it.

  *Context:* A generic extension point covering several submitted needs at once: virtual resources computed elsewhere, additional authorization mechanisms, delegated computation near the data, and interoperation bridges (WebDAV, CalDAV, ActivityPub). The hard parts are (a) how a visiting client authenticates through to the delegated endpoint and (b) how it verifies the endpoint is genuinely trusted by the storage owner; providers must be swappable without breaking clients (default endpoint discovery).

  *Other actors:* application developer, service provider.

  *Derived requirements:* [Discoverable Extension Endpoints](#req-extension-endpoints).

  *Sources:* [#207](https://github.com/w3c/lws-ucs/issues/207)

### Storage and resource management

- **<dfn id="uc-hypermedia-authoring">Hypermedia Authoring</dfn>** <span class="informative">(`UC-hypermedia-authoring` — Accepted)</span>

  **As an** application developer, **I want** consistent mechanisms for authoring hypermedia representations (e.g., JSON-LD, Siren), **so that** clients can navigate and interact with APIs uniformly.

  *Context:* Standardized hypermedia improves API usability.

  *Derived requirements:* [Self-Descriptive and Discoverable APIs](#req-self-descriptive-apis).

  *Sources:* [#33](https://github.com/w3c/lws-ucs/issues/33), [#124](https://github.com/w3c/lws-ucs/issues/124)

- **<dfn id="uc-storage-flexibility">Storage Flexibility</dfn>** <span class="informative">(`UC-storage-flexibility` — Accepted)</span>

  **As an** user, **I want** the ability to dynamically split or aggregate storage units, **so that** I can adjust capacity and organization as my needs evolve.

  *Context:* Flexible storage supports scalability and customization.

  *Derived requirements:* [Scalable Storage Management](#req-scalable-storage-management).

  *Sources:* [#69](https://github.com/w3c/lws-ucs/issues/69), [#70](https://github.com/w3c/lws-ucs/issues/70), [#110](https://github.com/w3c/lws-ucs/issues/110), [#127](https://github.com/w3c/lws-ucs/issues/127), [#136](https://github.com/w3c/lws-ucs/issues/136)

- **<dfn id="uc-storage-usage-insight">Storage Usage and Quota Insight</dfn>** <span class="informative">(`UC-storage-usage-insight` — Proposed)</span>

  **As an** user, **I want** to see how much space my storage uses, what is using it, and how much I have left, **so that** I can manage my storage before hitting a hard limit, and apps can warn me before a large write fails.

  *Context:* A storage manager (jeswr/solid-pod-manager) has no standard way to render a usage view: per-container sizes require walking the whole tree, and quota limits are provider-proprietary. Apps writing large data (media, scene files) equally need to distinguish 'quota exceeded' from other write failures, before or at write time. Needs: discoverable usage/quota metadata on the storage description, per-container aggregate size, and a structured quota-exceeded error.

  *Other actors:* application developer.

  *Derived requirements:* [Structured, Machine-Actionable Errors](#req-structured-errors), [Usage and Quota Discovery](#req-quota-discovery).

  *Sources:* [jeswr/solid-pod-manager](https://github.com/jeswr/solid-pod-manager)
