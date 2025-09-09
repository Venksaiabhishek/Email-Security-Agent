"""
Explainer Agent
Takes classification results (phishing, attachments, links)
and generates a clear explanation for the user.
"""

from google.adk.agents import LlmAgent

explainer_agent = LlmAgent(
    name="ExplainerAgent",
    model="gemini-2.0-flash",
    description="Explains why an email was flagged as phishing or safe.",
    instruction="""
    You are an Email Security Explainer.

    Input will contain:
    - if there is no input stay completely silent and do not reply.
    - Phishing classification result (PHISHING or LEGITIMATE with confidence)
    - Attachment analysis (SAFE, SUSPICIOUS, DANGEROUS)
    - Link analysis (SAFE, SUSPICIOUS, DANGEROUS)

    Task:
    - Summarize findings in plain English for the user.
    - Clearly explain why the email is flagged or considered safe.
    - Mention which attachments or links are problematic if any.

    Output:
    - A short paragraph explanation (3–5 sentences).
    """,
    output_key="explanation"
)