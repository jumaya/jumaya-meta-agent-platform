# MetaAgent.CloudAnalyzer

.NET 9 Minimal API service that analyzes architecture profiles and estimates cloud hosting costs.

## A2A Endpoint
`http://cloud-analyzer-svc:8006/.well-known/agent.json`

## Port
8006

## Supported Providers
- **Azure**: Container Apps, Azure SQL/Cosmos DB, CDN, Redis Cache
- **AWS**: ECS Fargate, RDS/DynamoDB, CloudFront, ElastiCache
- **Hostinger**: VPS KVM plans (most cost-effective for small projects)

## API Endpoints
- `GET /health` — Health check
- `GET /.well-known/agent.json` — A2A agent card
- `POST /a2a` — Estimate costs for given architecture
