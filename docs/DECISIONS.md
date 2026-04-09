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

## ADR-004: Model-Agnostic via LiteLLM + GitHub Models API
**Decision**: Use LiteLLM with a custom base URL pointing to the GitHub Models API.

**Rationale**: GitHub Copilot subscription provides access to all major models (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4, Gemini 2.5 Pro, etc.) via a single GitHub PAT. No separate API keys needed.

**Consequences**: Requires a GitHub PAT with Copilot access. LiteLlm routes all calls through `https://models.github.ai/inference`.

---

## ADR-005: MongoDB Atlas as Unified Persistence
**Decision**: Use MongoDB for all persistence including vector search for skill cache.

**Rationale**: Flexible schema for evolving project context. Built-in vector search avoids dedicated vector DB.

**Consequences**: MongoDB Atlas required for vector search. Local development uses community edition without vector search.

---

## ADR-006: Dynamic Skills from Internet
**Decision**: No local skill files. Skills fetched from internet via whitelist + cached in MongoDB.

**Rationale**: Always up-to-date best practices. No manual skill maintenance.

**Consequences**: Cache miss adds ~2s latency.

---

## ADR-013: LLM Provider — GitHub Models API
**Decision**: Use GitHub Models API via GitHub PAT. Single model for all agents configured via `MODEL` env var.

**Rationale**: GitHub Copilot subscription provides access to all major models via one PAT. No per-agent model selection. No external API keys needed.

**Consequences**: Requires a GitHub PAT with Copilot access. Model is set globally; not per-agent.

---

## ADR-014: Search Provider — DuckDuckGo
**Decision**: Use DuckDuckGo (`duckduckgo-search` Python package) instead of Bing Search.

**Rationale**: No API key, no registration, $0 cost. Identical search quality for developer queries.

**Consequences**: Rate limits apply to heavy usage. No SLA guarantees.

---

## ADR-007: One Visible Agent in VS Code
**Decision**: Only Meta Agent appears in VS Code Copilot Chat.

**Rationale**: Simplifies user experience. Users interact with one intelligent assistant, not a panel of specialists.

**Consequences**: Meta Agent must intelligently route all requests.
