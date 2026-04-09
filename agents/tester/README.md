# Tester Agent

Generates comprehensive test suites adapted to any test framework.

## A2A Endpoint
`http://tester-svc:8004/.well-known/agent.json`

## Port
8004

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `GITHUB_TOKEN` | - | GitHub Personal Access Token |
| `MODEL` | `claude-sonnet-4.6` | LLM model to use via GitHub Models API |
| `MONGODB_URI` | - | MongoDB connection string |
