# Architecture

## Overview

Meta AI Agent Platform v3 is a multi-agent system where specialized AI agents collaborate to deliver software engineering services. The architecture is designed for scalability, model-agnosticism, and extensibility.

## Components

### Orchestrator (Root Agent)
- Built with Google ADK `Agent`
- The only agent visible to the user via VS Code Copilot Chat
- Routes requests to specialized agents via `RemoteA2aAgent`
- Manages sequential pipelines for complex workflows

### Specialized Agents (Python)
Each agent is an independent Python service exposing an A2A endpoint:

| Agent | Port | Primary Model | Responsibility |
|-------|------|--------------|----------------|
| Architect | 8001 | claude-sonnet-4 | Architecture design via lean interview |
| Coder | 8003 | claude-sonnet-4 | Production-ready code generation |
| Tester | 8004 | gpt-4o-mini | Test suite generation |
| DevOps | 8005 | gpt-4o-mini | CI/CD and infrastructure as code |
| Security | 8007 | claude-sonnet-4 | OWASP security reviews |

### .NET Services
| Service | Port | Responsibility |
|---------|------|---------------|
| Scaffolder | 8002 | Project structure generation (.NET, Angular) |
| CloudAnalyzer | 8006 | Cloud cost estimation (Azure, AWS, Hostinger) |

### Skill Resolution Engine
Dynamic skill acquisition from trusted web sources:
1. Check MongoDB vector cache (TTL: 30 days)
2. Bing Search with domain whitelist
3. Fetch + extract with GPT-4o-mini
4. Cache embeddings for future similarity searches

### Persistence (MongoDB Atlas)
Collections:
- `project_contexts` — Project configurations and decisions
- `skill_cache` — Extracted skills with vector embeddings
- `sessions` — Pipeline execution state
- `source_whitelist` — Trusted domains for skill search
- `audit_log` — Token usage and agent actions

## Data Flow

```
User → Copilot Chat → Meta Agent (Orchestrator)
                              │
                    ┌─────────┴────────────┐
                    │  A2A Protocol        │
              ┌─────▼──┐          ┌───────▼────┐
              │ Python │          │ .NET 9     │
              │ Agents │          │ Services   │
              └─────┬──┘          └───────┬────┘
                    │                      │
              ┌─────▼──────────────────────▼────┐
              │         MongoDB Atlas            │
              │   Documents + Vector Search      │
              └──────────────────────────────────┘
```

## Kubernetes Deployment

- All services run as independent K8s Deployments
- Kustomize manages environment-specific configs
- HPA configured for orchestrator and coder in production
- MongoDB runs as StatefulSet with PVC
