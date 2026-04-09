# DevOps Agent

Generates CI/CD pipelines, Dockerfiles, and deployment configurations.

## A2A Endpoint
`http://devops-svc:8005/.well-known/agent.json`

## Port
8005

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `GITHUB_TOKEN` | - | GitHub Personal Access Token |
| `MODEL` | `claude-sonnet-4.6` | LLM model to use via GitHub Models API |
| `MONGODB_URI` | - | MongoDB connection string |
