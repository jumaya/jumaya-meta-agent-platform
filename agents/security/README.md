# Security Agent

Reviews code for OWASP vulnerabilities and security best practices.

## A2A Endpoint
`http://security-svc:8007/.well-known/agent.json`

## Port
8007

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `GITHUB_TOKEN` | - | GitHub Personal Access Token |
| `MODEL` | `claude-sonnet-4.6` | LLM model to use via GitHub Models API |
| `MONGODB_URI` | - | MongoDB connection string |
