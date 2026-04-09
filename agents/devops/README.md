# DevOps Agent

Generates CI/CD pipelines, Dockerfiles, and deployment configurations.

## A2A Endpoint
`http://devops-svc:8005/.well-known/agent.json`

## Port
8005

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `DEVOPS_MODEL` | `openai/gpt-4o-mini` | LLM model to use |
| `MONGODB_URI` | - | MongoDB connection string |
| `OPENAI_API_KEY` | - | OpenAI API key |
