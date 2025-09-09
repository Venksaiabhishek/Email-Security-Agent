from google.adk.agents import SequentialAgent
from .classifier.agent import classifier_agent
from .explainer.agent import explainer_agent
from .advisor.agent import advisor_agent
from .greeting.agent import greeting_agent
# Root agent orchestrating the flow
root_agent = SequentialAgent(
    name="EmailSecurityRootAgent",
    description="Runs classification, explanation, and advice in sequence.",
    sub_agents=[
        greeting_agent,
        classifier_agent,
        explainer_agent,
        advisor_agent,
        
    ]
)