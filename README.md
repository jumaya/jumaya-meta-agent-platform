# Meta AI Agent Platform v3

[![CI Agents](https://github.com/jumaya/jumaya-meta-agent-platform/actions/workflows/ci-agents.yml/badge.svg)](https://github.com/jumaya/jumaya-meta-agent-platform/actions/workflows/ci-agents.yml)
[![CI Services](https://github.com/jumaya/jumaya-meta-agent-platform/actions/workflows/ci-services.yml/badge.svg)](https://github.com/jumaya/jumaya-meta-agent-platform/actions/workflows/ci-services.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

> **AI-Powered Software Engineering Consultancy** — Google ADK · A2A Protocol · .NET 9 · Kubernetes

An intelligent multi-agent platform that acts as your software engineering team. Interact through **VS Code + GitHub Copilot Chat** to design architecture, generate production-ready code, create test suites, set up CI/CD pipelines, analyze cloud costs, and review security.

## Architecture Overview

```
VS Code + GitHub Copilot Chat
           │
           ▼
    ┌─────────────────┐
    │  Meta Agent     │  ← Root orchestrator (Google ADK)
    │  (Orchestrator) │
    └────────┬────────┘
             │ A2A Protocol
    ┌────────┼────────────────────────────────┐
    │        │                                │
    ▼        ▼        ▼        ▼        ▼     ▼
Architect  Coder   Tester  DevOps  Security  Cloud
 (Python)  (Python)(Python)(Python)(Python) Analyzer
                                            (.NET 9)
    ▲
    │ A2A
Scaffolder
(.NET 9)
```

All agents are independent services communicating via the **A2A (Agent-to-Agent) protocol**. The user sees **only one agent** in VS Code Copilot Chat — Meta Agent — which routes tasks internally.

## Quick Start

### Prerequisites
- Docker + Docker Compose
- Python 3.12+
- .NET 9 SDK
- API Keys: Google AI, OpenAI, Anthropic, Bing Search

### Development
```bash
# 1. Copy environment template
cp .env.example .env
# Edit .env with your API keys

# 2. Start all services
make dev-up

# 3. Open VS Code and use Meta Agent in Copilot Chat
# Example: "Create a new gym management system in .NET 9 with Angular"
```

## Stack

| Layer | Technology |
|-------|-----------|
| Agent Orchestration | Google ADK (Agent Development Kit) |
| Agent Communication | A2A Protocol |
| Python Agents | Python 3.12, google-adk[a2a], litellm |
| .NET Services | .NET 9, Minimal API |
| Persistence | MongoDB Atlas (documents + vector search) |
| Infrastructure | Kubernetes + Kustomize |
| VS Code Integration | GitHub Copilot Chat (`.agent.md`) |

## Model Presets

| Preset | Cost/Pipeline | Use Case |
|--------|--------------|----------|
| **Budget** | ~$0.01 | Prototypes, exploration |
| **Auto** | ~$0.04 | Daily development (recommended) |
| **Premium** | ~$0.08 | Production-critical code |

## Project Structure

```
agents/          ← Python agents (Google ADK + A2A)
  shared/        ← Shared tools, services, config
  orchestrator/  ← Root agent + pipelines
  architect/     ← Architecture advisor
  coder/         ← Code generator
  tester/        ← Test generator
  devops/        ← CI/CD generator
  security/      ← Security reviewer
services/        ← .NET 9 services (A2A compatible)
  MetaAgent.Scaffolder/     ← Project scaffolding
  MetaAgent.CloudAnalyzer/  ← Cloud cost analysis
k8s/             ← Kubernetes manifests (Kustomize)
.github/         ← CI/CD workflows + Copilot agent definition
docs/            ← Architecture, decisions, setup guides
```

## License

Apache 2.0 — see [LICENSE](LICENSE)

> AI-Powered Software Engineering Consultancy — Google ADK + A2A + .NET 9 + Kubernetes

🚧 **Scaffolding in progress...** — Full project structure coming in the next PR.