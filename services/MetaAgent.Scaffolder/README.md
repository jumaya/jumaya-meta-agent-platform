# MetaAgent.Scaffolder

.NET 9 Minimal API service that generates complete project structures via the A2A protocol.

## A2A Endpoint
`http://scaffolder-svc:8002/.well-known/agent.json`

## Port
8002

## Supported Templates
- `.NET 9 Clean Architecture` (Domain + Application + Infrastructure + API layers)
- `Angular 18 Standalone` (standalone components, lazy routes)

## API Endpoints
- `GET /health` — Health check
- `GET /.well-known/agent.json` — A2A agent card
- `POST /a2a` — Process A2A scaffolding requests
