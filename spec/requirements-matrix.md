<!-- GENERATED from ucr/*.ttl by scripts/generate-spec-md.py — DO NOT EDIT BY HAND.
     Edit the Turtle corpus and regenerate (python3 scripts/generate-spec-md.py). -->

### Traceability

Generated from the corpus: **83 use cases**, **73 requirements**, **143 motivation links** (each machine-validated: every requirement traces to at least one use case).

| Use case | Status | Derived requirements |
| --- | --- | --- |
| ['Bring Your Own Data' Apps](#uc-byod-apps) | Accepted | [Self-Descriptive and Discoverable APIs](#req-self-descriptive-apis) |
| ['End to End' Encryption](#uc-e2e-encryption) | Accepted | [End-to-End Encryption](#req-e2e-encryption) |
| [Administrative Assistant](#uc-administrative-assistant) | Accepted | [Auditable Trail](#req-auditable-trail), [Delegation of Access Rights](#req-delegation-of-access-rights) |
| [AI Agent Access to Storage](#uc-ai-agent-access) | Proposed | [Attribution of Writes](#req-write-attribution), [Auditable Trail](#req-auditable-trail), [Least-Privilege Scoped Credentials](#req-scoped-access) |
| [API Protocol Decoupling](#uc-api-protocol-decoupling) | Accepted | [Loose Coupling of Underlying Protocols](#req-protocol-decoupling) |
| [Application Notifications](#uc-application-notifications) | Accepted | [Subscribing to Resource Changes (Notifications)](#req-change-notifications) |
| [Authentication Mechanism(s)](#uc-authentication-mechanisms) | Accepted | [Authentication Mechanisms](#req-authentication-mechanisms), [Silent Session Continuation](#req-silent-reauth) |
| [Backend Service Integration](#uc-backend-service-integration) | Accepted | [Server-to-Server Authentication](#req-server-to-server-auth) |
| [Binary Asset with Linked Descriptor](#uc-binary-asset-descriptor) | Proposed | [Byte-Exact Non-RDF Resource Fidelity](#req-binary-fidelity), [Descriptive Metadata Without Touching the Resource](#req-paired-metadata) |
| [Business Data Access](#uc-business-data-access) | Accepted | [Access Request Handling](#req-access-request-handling) |
| [Clear Error Messages](#uc-clear-error-messages) | Accepted | [Structured, Machine-Actionable Errors](#req-structured-errors) |
| [Consent-Based Sharing](#uc-consent-based-sharing) | Accepted | [Consent-Based Data Sharing](#req-consent-based-sharing), [Usage Control Policies](#req-usage-control) |
| [Context-Aware Access Policies](#uc-context-aware-access-policies) | Accepted | [Contextual Access Control](#req-contextual-access-control) |
| [Contextual Interactions](#uc-contextual-interactions) | Accepted | — |
| [Crawling and Indexing Public Storage Data](#uc-public-index-crawl) | Proposed | [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Inbox (Notifications)](#req-inbox), [Indexing Control](#req-indexing-control), [Rate-Limit Signaling](#req-rate-limit-signaling) |
| [CRDT Update Log in Storage](#uc-crdt-collaboration-log) | Proposed | [Collaborative Editing](#req-collaborative-editing), [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Indexing Control](#req-indexing-control) |
| [Cross-Application Data Interoperability](#uc-cross-app-interop) | Proposed | [Attribution of Writes](#req-write-attribution), [Data Location Registry](#req-app-data-registry), [Serialization Format](#req-serialization-format) |
| [Custom Validation of Mutating Requests](#uc-mutation-validation) | Proposed | [Server-Side Write Validation](#req-write-validation) |
| [Data Integration](#uc-data-integration) | Accepted | [Federated Data Queries](#req-federated-queries), [Federated Query Joins](#req-federated-query-joins), [Serialization Format](#req-serialization-format) |
| [Delegating Control of a Storage](#uc-delegation-of-control) | Accepted | [Delegation of Control](#req-delegation-of-control), [Transfer of Control](#req-transfer-of-control) |
| [Deletion Visibility for Replicas](#uc-replica-deletion-sync) | Proposed | [Deletion and Move Signaling](#req-deletion-signaling), [Offline Access and Synchronization](#req-offline-sync) |
| [Digital Goods Delivery](#uc-digital-goods-delivery) | Accepted | [Auditable Trail](#req-auditable-trail) |
| [Discovering Where Data Lives](#uc-app-data-discovery) | Proposed | [Data Location Registry](#req-app-data-registry), [Non-Leaky Discovery](#req-non-leaky-discovery) |
| [Discovering Who Has Access](#uc-access-overview) | Proposed | [Authorization Enumeration](#req-authorization-enumeration) |
| [Durable Save on Exit](#uc-durable-exit-save) | Proposed | [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Performance and Scalability](#req-performance-scalability) |
| [Fail-Closed Provisioning of App Data](#uc-fail-closed-provisioning) | Proposed | [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Fail-Closed Creation Semantics](#req-secure-defaults) |
| [Federated Task Dashboard](#uc-federated-task-dashboard) | Proposed | [Data Location Registry](#req-app-data-registry), [Federated Data Queries](#req-federated-queries), [Subscribing to Resource Changes (Notifications)](#req-change-notifications) |
| [Generic Storage](#uc-generic-storage) | Accepted | [Adding, Updating, Deleting Resources in Storage](#req-resource-crud), [Resource Versioning](#req-resource-versioning) |
| [Globally Unique Identity](#uc-globally-unique-identifiers) | Accepted | [Globally Unique Identifiers](#req-globally-unique-identifiers) |
| [Group Sharing](#uc-group-sharing) | Accepted | [Data Sharing](#req-data-sharing), [Group-Based Access Control](#req-group-access-control) |
| [Health Record Access](#uc-health-record-access) | Accepted | [Access Request Handling](#req-access-request-handling), [Auditable Trail](#req-auditable-trail), [Data Sharing](#req-data-sharing), [Delegation of Access Rights](#req-delegation-of-access-rights) |
| [Home Access](#uc-home-access) | Accepted | — |
| [Hypermedia Authoring](#uc-hypermedia-authoring) | Accepted | [Self-Descriptive and Discoverable APIs](#req-self-descriptive-apis) |
| [ID Alias](#uc-id-alias) | Proposed | [Globally Unique Identifiers](#req-globally-unique-identifiers) |
| [Identity & Credentials Management](#uc-identity-credentials-management) | Accepted | [Authentication Mechanisms](#req-authentication-mechanisms) |
| [Indexed and Non-Indexed Data](#uc-selective-indexing) | Proposed | [Indexing Control](#req-indexing-control) |
| [Indexing a Volunteer Profile](#uc-profile-indexing) | Proposed | [Consent-Based Data Sharing](#req-consent-based-sharing), [Subscribing to Resource Changes (Notifications)](#req-change-notifications), [Usage Control Policies](#req-usage-control) |
| [Institutional Records Provability](#uc-institutional-records) | Proposed | [Data Integrity Verification](#req-data-integrity-verification), [Deletion and Move Signaling](#req-deletion-signaling), [Immutable Resource Snapshots](#req-immutable-snapshots), [Verified References to External Resources](#req-verified-references) |
| [Key-Value Mirror with Atomic Hydration](#uc-kv-mirror-hydrate) | Proposed | [Atomic Multi-Resource Operations](#req-atomic-batch), [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Pagination, Filtering and Sorting](#req-paginate-filter-sort) |
| [Large File Uploads](#uc-large-file-uploads) | Accepted | [Resumable Large Data Transfers](#req-resumable-uploads) |
| [Legal Grounds Support](#uc-legal-grounds-support) | Accepted | [Legal Basis Enforcement](#req-legal-basis-enforcement) |
| [Legal Reporting](#uc-legal-reporting) | Accepted | [Auditable Trail](#req-auditable-trail), [Data Integrity Verification](#req-data-integrity-verification) |
| [Local Data About Foreign Identifiers](#uc-foreign-identifier-data) | Proposed | [Access to Data About External Identifiers](#req-external-identifier-access) |
| [Markers for Moved or Deleted Resources](#uc-link-preservation) | Proposed | [Deletion and Move Signaling](#req-deletion-signaling) |
| [Media Playback from Storage](#uc-media-streaming) | Proposed | [Byte-Exact Non-RDF Resource Fidelity](#req-binary-fidelity), [Partial-Content Reads](#req-range-requests) |
| [Meeting Scheduling](#uc-meeting-scheduling) | Accepted | [Inbox (Notifications)](#req-inbox) |
| [Migrating an Existing App onto User Storage](#uc-legacy-app-migration) | Proposed | [Browser Access from Foreign Origins](#req-cors-browser-access), [Fail-Closed Creation Semantics](#req-secure-defaults), [Serialization Format](#req-serialization-format), [Stable, Verifiable Application Identity](#req-app-identity) |
| [Notifications for Permission Changes](#uc-permission-change-notifications) | Accepted | [Subscribing to Resource Changes (Notifications)](#req-change-notifications) |
| [Offline Data Access](#uc-offline-data-access) | Accepted | [Offline Access and Synchronization](#req-offline-sync) |
| [Offline-First Instant Load](#uc-offline-first-instant-load) | Proposed | [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Offline Access and Synchronization](#req-offline-sync), [Subscribing to Resource Changes (Notifications)](#req-change-notifications) |
| [Optimistic, Non-Blocking Saves](#uc-optimistic-concurrency) | Proposed | [Conditional Requests and Optimistic Concurrency](#req-conditional-requests), [Structured, Machine-Actionable Errors](#req-structured-errors) |
| [Pagination & Filtering](#uc-pagination-filtering) | Accepted | [Pagination, Filtering and Sorting](#req-paginate-filter-sort), [Search and Query](#req-search-and-query) |
| [Performant Access Control](#uc-performant-access-control) | Accepted | [Performance and Scalability](#req-performance-scalability) |
| [Permission-Aware User Interface](#uc-permission-aware-ui) | Proposed | [Effective-Permission Introspection](#req-permission-introspection) |
| [Personal Information Management](#uc-personal-information-management) | Accepted | [Personal Data Projection](#req-personal-data-projection), [Serialization Format](#req-serialization-format) |
| [Polling](#uc-polling) | Accepted | — |
| [Portable Storage](#uc-storage-portability) | Accepted | [Storage Portability](#req-storage-portability) |
| [Privacy in Data Discovery](#uc-private-data-discovery) | Proposed | [Non-Leaky Discovery](#req-non-leaky-discovery) |
| [Profile Sharing](#uc-profile-sharing) | Accepted | [Data Sharing](#req-data-sharing), [Profile Management](#req-profile-management) |
| [Pseudonymous Access for Vendors](#uc-pseudonymous-access) | Proposed | [Pseudonymous Identifiers](#req-pseudonymity) |
| [Real-Time Notifications](#uc-real-time-notifications) | Accepted | [Subscribing to Resource Changes (Notifications)](#req-change-notifications) |
| [Recognizable Application Identity](#uc-recognizable-app-identity) | Proposed | [Stable, Verifiable Application Identity](#req-app-identity) |
| [Renaming / Moving a Resource or Container](#uc-resource-rename-move) | Proposed | [Deletion and Move Signaling](#req-deletion-signaling), [Server-Side Rename and Move](#req-rename-move) |
| [Search Functionality](#uc-search-functionality) | Accepted | [Metadata Query](#req-metadata-query), [Pagination, Filtering and Sorting](#req-paginate-filter-sort), [Pod-Level Query](#req-pod-level-query), [Query Other Storages](#req-query-other-pods), [Resource-Level Query](#req-resource-level-query), [Search and Query](#req-search-and-query) |
| [Semantic Collaboration](#uc-semantic-collaboration) | Accepted | [Collaborative Editing](#req-collaborative-editing) |
| [Sensor Data Sharing](#uc-sensor-data-sharing) | Accepted | [View-Based Data Sharing](#req-view-based-sharing) |
| [Sharing Access](#uc-sharing-access) | Accepted | [Data Sharing](#req-data-sharing) |
| [Silent Session Restore](#uc-silent-session-restore) | Proposed | [Silent Session Continuation](#req-silent-reauth) |
| [SPARQL Queries](#uc-sparql-queries) | Accepted | [Federated Data Queries](#req-federated-queries), [Federated Query Joins](#req-federated-query-joins), [Pagination, Filtering and Sorting](#req-paginate-filter-sort), [Pod-Level Query](#req-pod-level-query), [Query Other Storages](#req-query-other-pods), [Resource-Level Query](#req-resource-level-query), [Search and Query](#req-search-and-query) |
| [Storage Description and Discovery](#uc-storage-description-discovery) | Accepted | [Self-Descriptive and Discoverable APIs](#req-self-descriptive-apis) |
| [Storage Flexibility](#uc-storage-flexibility) | Accepted | [Scalable Storage Management](#req-scalable-storage-management) |
| [Storage Listening](#uc-storage-listening) | Accepted | [Offline Access and Synchronization](#req-offline-sync) |
| [Storage Ownership](#uc-storage-ownership) | Accepted | [Control of Storages](#req-control-of-storages) |
| [Storage Usage and Quota Insight](#uc-storage-usage-insight) | Proposed | [Structured, Machine-Actionable Errors](#req-structured-errors), [Usage and Quota Discovery](#req-quota-discovery) |
| [Timeseries Storage](#uc-timeseries-storage) | Accepted | [Timeseries Data Support](#req-timeseries) |
| [Trust Mechanism for Storage Providers](#uc-storage-provider-trust) | Accepted | [Trusted Identity Providers](#req-trusted-identity-providers), [Use of Service Providers](#req-service-providers) |
| [Universal Communication](#uc-universal-communication) | Accepted | [Inbox (Notifications)](#req-inbox) |
| [Usage Control](#uc-usage-control) | Proposed | [Usage Control Policies](#req-usage-control) |
| [User-Defined Custom API Endpoints](#uc-custom-api-endpoints) | Proposed | [Discoverable Extension Endpoints](#req-extension-endpoints) |
| [User-Owned Agent Memory](#uc-agent-memory) | Proposed | [Attribution of Writes](#req-write-attribution), [Least-Privilege Scoped Credentials](#req-scoped-access) |
| [WebID Profile Interaction](#uc-webid-profile-interaction) | Accepted | [Profile Interaction UI](#req-profile-interaction-ui) |
| [Website Creation](#uc-website-creation) | Accepted | [Self-Describing Website Publication](#req-website-publication) |
| [Workflow Automation over Storage](#uc-workflow-automation) | Proposed | [Least-Privilege Scoped Credentials](#req-scoped-access), [Rate-Limit Signaling](#req-rate-limit-signaling), [Server-to-Server Authentication](#req-server-to-server-auth), [Structured, Machine-Actionable Errors](#req-structured-errors) |

The following use cases are not yet covered by any requirement: [Contextual Interactions](#uc-contextual-interactions), [Home Access](#uc-home-access), [Polling](#uc-polling).
