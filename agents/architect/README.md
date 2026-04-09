# Architect Agent

Analyzes project requirements through a lean 5-question interview and produces architecture recommendations.

## A2A Endpoint
`http://architect-svc:8001/.well-known/agent.json`

## Port
8001

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `GITHUB_TOKEN` | - | GitHub Personal Access Token |
| `MODEL` | `claude-sonnet-4.6` | LLM model to use via GitHub Models API |
| `MONGODB_URI` | - | MongoDB connection string |
