.PHONY: dev-up dev-down build test deploy lint fmt help

DOCKER_COMPOSE = docker compose -f docker-compose.dev.yml
KUSTOMIZE_DIR = k8s/overlays/dev

help:
	@echo "Meta AI Agent Platform v3 — Available commands:"
	@echo ""
	@echo "  make dev-up      Start all services locally (Docker Compose)"
	@echo "  make dev-down    Stop all services"
	@echo "  make build       Build all Docker images"
	@echo "  make test        Run all tests (Python + .NET)"
	@echo "  make deploy      Deploy to Kubernetes (dev overlay)"
	@echo "  make lint        Run linters (ruff + dotnet format)"
	@echo "  make fmt         Format code (ruff format + dotnet format)"
	@echo ""

dev-up:
	$(DOCKER_COMPOSE) up --build -d
	@echo "Services started. Check logs with: make logs"

dev-down:
	$(DOCKER_COMPOSE) down -v

logs:
	$(DOCKER_COMPOSE) logs -f

build:
	$(DOCKER_COMPOSE) build

test: test-python test-dotnet

test-python:
	@echo "Running Python tests..."
	cd agents && python -m pytest --tb=short -q

test-dotnet:
	@echo "Running .NET tests..."
	cd services && dotnet test MetaAgent.sln --no-build --verbosity minimal

lint:
	@echo "Linting Python..."
	cd agents && ruff check .
	@echo "Linting .NET..."
	cd services && dotnet format --verify-no-changes

fmt:
	@echo "Formatting Python..."
	cd agents && ruff format .
	@echo "Formatting .NET..."
	cd services && dotnet format

deploy:
	kubectl apply -k $(KUSTOMIZE_DIR)
	@echo "Deployed to Kubernetes (dev)"

deploy-prod:
	kubectl apply -k k8s/overlays/prod
	@echo "Deployed to Kubernetes (prod)"

rollout-status:
	kubectl rollout status deployment -n meta-agent

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
