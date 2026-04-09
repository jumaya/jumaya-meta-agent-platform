import os

from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models.lite_llm import LiteLlm

from shared.config.settings import settings

os.environ.setdefault("OPENAI_API_KEY", settings.github_token)
os.environ.setdefault("OPENAI_API_BASE", "https://models.github.ai/inference")

architect = RemoteA2aAgent(
    name="architect",
    description="Analyzes requirements and designs architecture through a lean interview process",
    agent_card=os.getenv("ARCHITECT_AGENT_CARD", "http://architect-svc:8001/.well-known/agent.json"),
)
scaffolder = RemoteA2aAgent(
    name="scaffolder",
    description="Generates project structure and scaffolding for any stack",
    agent_card=os.getenv("SCAFFOLDER_AGENT_CARD", "http://scaffolder-svc:8002/.well-known/agent.json"),
)
coder = RemoteA2aAgent(
    name="coder",
    description="Generates production-ready code for any language and framework",
    agent_card=os.getenv("CODER_AGENT_CARD", "http://coder-svc:8003/.well-known/agent.json"),
)
tester = RemoteA2aAgent(
    name="tester",
    description="Generates comprehensive test suites adapted to any test framework",
    agent_card=os.getenv("TESTER_AGENT_CARD", "http://tester-svc:8004/.well-known/agent.json"),
)
devops = RemoteA2aAgent(
    name="devops",
    description="Generates CI/CD pipelines, Dockerfiles, and deployment configurations",
    agent_card=os.getenv("DEVOPS_AGENT_CARD", "http://devops-svc:8005/.well-known/agent.json"),
)
cloud_analyzer = RemoteA2aAgent(
    name="cloud_analyzer",
    description="Analyzes architecture and estimates cloud hosting costs across providers",
    agent_card=os.getenv(
        "CLOUD_ANALYZER_AGENT_CARD", "http://cloud-analyzer-svc:8006/.well-known/agent.json"
    ),
)
security = RemoteA2aAgent(
    name="security",
    description="Reviews code for OWASP vulnerabilities and security best practices",
    agent_card=os.getenv("SECURITY_AGENT_CARD", "http://security-svc:8007/.well-known/agent.json"),
)

root_agent = Agent(
    model=LiteLlm(model=f"openai/{settings.model}"),
    name="meta_agent",
    instruction="""You are Meta Agent, an AI-powered software engineering consultant.
    You help developers create, build, test, deploy, and secure software projects.

    Route user requests to the appropriate agent or pipeline:
    - "Create a new project..." → delegate to architect first, then scaffolder, coder, tester
    - "Generate code for..." → delegate to coder
    - "Add tests..." → delegate to tester
    - "Set up CI/CD..." or "Deploy..." → delegate to devops
    - "How much would it cost to host..." → delegate to cloud_analyzer
    - "Review security..." → delegate to security
    - "Design the architecture..." → delegate to architect

    Always respond in the user's language. System processing is in English for token efficiency.
    Keep responses concise and actionable.
    """,
    sub_agents=[architect, scaffolder, coder, tester, devops, cloud_analyzer, security],
)
