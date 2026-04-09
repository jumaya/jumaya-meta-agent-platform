# Tester Agent

Generates comprehensive test suites adapted to any test framework.

## A2A Endpoint
`http://tester-svc:8004/.well-known/agent.json`

## Port
8004

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `TESTER_MODEL` | `openai/gpt-4o-mini` | LLM model to use |
| `MONGODB_URI` | - | MongoDB connection string |
| `OPENAI_API_KEY` | - | OpenAI API key |
