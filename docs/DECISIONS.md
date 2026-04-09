# Architecture Decision Records

## ADR-001: Google ADK as Agent Framework
**Decision**: Use Google ADK (Agent Development Kit) for Python agent orchestration.

**Rationale**: ADK provides built-in support for A2A protocol, sequential/parallel agents, dynamic instructions via `ReadonlyContext`, and `RemoteA2aAgent` for cross-service delegation.

**Consequences**: Dependency on Google ADK API stability. Agents run as ADK API servers.

---

## ADR-002: A2A Protocol for Agent Communication
**Decision**: Each specialized agent is an independent service communicating via A2A.

**Rationale**: A2A enables agent independence, polyglot services (.NET + Python), independent scaling, and fault isolation.

**Consequences**: Network latency between agents. Requires service discovery (K8s Services).

---

## ADR-003: Hybrid Stack (Python + .NET 9)
**Decision**: Python for AI orchestration, .NET 9 for scaffolding and pricing services.

**Rationale**: .NET excels at template generation and API integration. Python has the best AI/LLM ecosystem.

**Consequences**: Two build systems. Developers need both Python and .NET skills.

---

## ADR-004: Model-Agnostic via LiteLLM
**Decision**: Use LiteLLM to abstract LLM provider calls.

**Rationale**: Enables switching between OpenAI, Anthropic, and Google models without code changes.

**Consequences**: LiteLLM adds ~50ms latency per call. Provider API keys required.

---

## ADR-005: MongoDB Atlas as Unified Persistence
**Decision**: Use MongoDB for all persistence including vector search for skill cache.

**Rationale**: Flexible schema for evolving project context. Built-in vector search avoids dedicated vector DB.

**Consequences**: MongoDB Atlas required for vector search. Local development uses community edition without vector search.

---

## ADR-006: Dynamic Skills from Internet
**Decision**: No local skill files. Skills fetched from internet via whitelist + cached in MongoDB.

**Rationale**: Always up-to-date best practices. No manual skill maintenance.

**Consequences**: Requires Bing Search API key. Cache miss adds ~2s latency.

---

## ADR-007: One Visible Agent in VS Code
**Decision**: Only Meta Agent appears in VS Code Copilot Chat.

**Rationale**: Simplifies user experience. Users interact with one intelligent assistant, not a panel of specialists.

**Consequences**: Meta Agent must intelligently route all requests.
