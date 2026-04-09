# Security Agent

Reviews code for OWASP vulnerabilities and security best practices.

## A2A Endpoint
`http://security-svc:8007/.well-known/agent.json`

## Port
8007

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `SECURITY_MODEL` | `anthropic/claude-sonnet-4-20250514` | LLM model to use |
| `MONGODB_URI` | - | MongoDB connection string |
| `ANTHROPIC_API_KEY` | - | Anthropic API key |
