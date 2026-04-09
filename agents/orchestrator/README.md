# Orchestrator Agent

Root agent that routes user requests to specialized sub-agents via the A2A protocol.

## Responsibilities
- Receives user requests from VS Code Copilot Chat
- Routes to appropriate specialized agents
- Manages sequential pipelines for complex workflows
- Handles model preset selection on first interaction

## Pipelines
- `new_project_pipeline`: architect → scaffolder → coder → tester
- `add_feature_pipeline`: architect → coder → tester
- `deploy_pipeline`: cloud_analyzer → devops → security
- `review_pipeline`: security

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `ARCHITECT_AGENT_CARD` | `http://architect-svc:8001/.well-known/agent.json` | Architect A2A card URL |
| `CODER_AGENT_CARD` | `http://coder-svc:8003/.well-known/agent.json` | Coder A2A card URL |
| `TESTER_AGENT_CARD` | `http://tester-svc:8004/.well-known/agent.json` | Tester A2A card URL |
| `DEVOPS_AGENT_CARD` | `http://devops-svc:8005/.well-known/agent.json` | DevOps A2A card URL |
| `CLOUD_ANALYZER_AGENT_CARD` | `http://cloud-analyzer-svc:8006/.well-known/agent.json` | Cloud Analyzer A2A card URL |
| `SECURITY_AGENT_CARD` | `http://security-svc:8007/.well-known/agent.json` | Security A2A card URL |
