from google.adk.agents import ParallelAgent, LlmAgent

# existing LLM agents for links and attachments
from .subagents.link_checker.agent import link_checker_agent
from .subagents.attachment_checker.agent import attachment_checker_agent
from .subagents.phishing_email_detector.agent import phishing_email_detector_agent


classifier_agent = ParallelAgent(
    name="ClassifierAgent",
    description="Runs phishing detector, attachment checker, and link checker concurrently.",
    sub_agents=[phishing_email_detector_agent, attachment_checker_agent, link_checker_agent],
    
)