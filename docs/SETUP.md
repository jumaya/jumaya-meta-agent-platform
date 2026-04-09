# Setup Guide

## Prerequisites

- **Python 3.12+**
- **.NET 9 SDK**
- **Docker + Docker Compose**
- **kubectl** (for K8s deployment)
- **API Keys**:
  - `GOOGLE_API_KEY` — Google AI Studio
  - `OPENAI_API_KEY` — OpenAI Platform
  - `ANTHROPIC_API_KEY` — Anthropic Console
  - `BING_SEARCH_KEY` — Azure Cognitive Services (Bing Search v7)

## Local Development

### 1. Clone and configure
```bash
git clone https://github.com/jumaya/jumaya-meta-agent-platform.git
cd jumaya-meta-agent-platform
cp .env.example .env
# Edit .env with your API keys
```

### 2. Start services
```bash
make dev-up
```

This starts:
- MongoDB on port 27017
- Orchestrator on port 8000
- Architect on port 8001
- Scaffolder on port 8002
- Coder on port 8003
- Tester on port 8004
- DevOps on port 8005
- Cloud Analyzer on port 8006
- Security on port 8007

### 3. Configure VS Code

Install the GitHub Copilot Chat extension. The `.github/agents/meta-agent.agent.md` file registers Meta Agent automatically.

In Copilot Chat, select **Meta Agent** from the agent picker and start:

```
Create a new gym management system in .NET 9 with Angular 18
```

## Kubernetes Deployment

### Prerequisites
- Kubernetes cluster (AKS, EKS, GKE, or local k3s)
- `kubectl` configured
- Container registry access

### Deploy to dev
```bash
# Build and push images first (see CI/CD)
make deploy
```

### Deploy to prod
```bash
make deploy-prod
```

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | Yes | Google Gemini API key |
| `OPENAI_API_KEY` | Yes | OpenAI API key |
| `ANTHROPIC_API_KEY` | Yes | Anthropic API key |
| `BING_SEARCH_KEY` | Yes | Bing Search v7 API key |
| `MONGODB_URI` | Yes | MongoDB connection string |
| `DEFAULT_MODEL_PRESET` | No | `auto` (default), `budget`, or `premium` |
| `SKILL_CACHE_TTL_DAYS` | No | `30` (default) |
| `LOG_LEVEL` | No | `INFO` (default) |
