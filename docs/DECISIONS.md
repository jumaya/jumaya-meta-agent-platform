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

**Consequences**: Cache miss adds ~2s latency.

---

## ADR-007: One Visible Agent in VS Code
**Decision**: Only Meta Agent appears in VS Code Copilot Chat.

**Rationale**: Simplifies user experience. Users interact with one intelligent assistant, not a panel of specialists.

**Consequences**: Meta Agent must intelligently route all requests.

---

## ADR-013: LLM Provider — GitHub Models API
**Decision**: Use GitHub Models API (`https://models.github.ai/inference`) authenticated with a GitHub Personal Access Token instead of individual OpenAI/Anthropic/Google API keys.

**Rationale**: Users with a GitHub Copilot subscription get access to all major models (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4, Gemini 2.5 Pro, GPT-4o, etc.) through a single GitHub PAT. This eliminates the need to manage multiple API keys and provider accounts. A single `MODEL` env var controls which model all agents use.

**Consequences**: Requires a GitHub Copilot subscription. All LLM traffic routes through GitHub Models API endpoint. Model selection is uniform — all agents use the same configured model.

---

## ADR-014: Search Provider — DuckDuckGo
**Decision**: Replace Bing Search with DuckDuckGo (`duckduckgo-search` Python package) for the Skill Resolution Engine.

**Rationale**: DuckDuckGo requires no API key, no registration, and costs $0. This removes a mandatory dependency and simplifies setup for new contributors.

**Consequences**: No account or billing setup required. Search quality is comparable for technical queries. Results may differ slightly from Bing.
