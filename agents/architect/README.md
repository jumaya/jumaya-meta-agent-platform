# Architect Agent

Analyzes project requirements through a lean 5-question interview and produces architecture recommendations.

## A2A Endpoint
`http://architect-svc:8001/.well-known/agent.json`

## Port
8001

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `ARCHITECT_MODEL` | `anthropic/claude-sonnet-4-20250514` | LLM model to use |
| `MONGODB_URI` | - | MongoDB connection string |
| `ANTHROPIC_API_KEY` | - | Anthropic API key |
