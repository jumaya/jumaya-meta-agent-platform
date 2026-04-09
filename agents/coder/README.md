# Coder Agent

Generates production-ready code for any language and framework.

## A2A Endpoint
`http://coder-svc:8003/.well-known/agent.json`

## Port
8003

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `GITHUB_TOKEN` | - | GitHub Personal Access Token |
| `MODEL` | `claude-sonnet-4.6` | LLM model to use via GitHub Models API |
| `MONGODB_URI` | - | MongoDB connection string |
