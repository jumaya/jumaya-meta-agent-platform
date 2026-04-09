# Coder Agent

Generates production-ready code for any language and framework.

## A2A Endpoint
`http://coder-svc:8003/.well-known/agent.json`

## Port
8003

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `CODER_MODEL` | `anthropic/claude-sonnet-4-20250514` | LLM model to use |
| `MONGODB_URI` | - | MongoDB connection string |
| `ANTHROPIC_API_KEY` | - | Anthropic API key |
