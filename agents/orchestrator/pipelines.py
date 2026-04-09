from google.adk.agents.sequential_agent import SequentialAgent

from .agent import architect, cloud_analyzer, coder, devops, scaffolder, security, tester

new_project_pipeline = SequentialAgent(
    name="new_project_pipeline",
    description="Full pipeline: architecture → scaffolding → code → tests",
    sub_agents=[architect, scaffolder, coder, tester],
)

add_feature_pipeline = SequentialAgent(
    name="add_feature_pipeline",
    description="Add feature: architecture review → code → tests",
    sub_agents=[architect, coder, tester],
)

deploy_pipeline = SequentialAgent(
    name="deploy_pipeline",
    description="Deploy: cost analysis → CI/CD → security review",
    sub_agents=[cloud_analyzer, devops, security],
)

review_pipeline = SequentialAgent(
    name="review_pipeline",
    description="Review: security audit",
    sub_agents=[security],
)
