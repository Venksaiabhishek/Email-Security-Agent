from google.adk.agents import LlmAgent

greeting_agent = LlmAgent(
    name="GreetingAgent",
    description="Handles simple greetings like hi/hello",
    instruction="""
    If the user greets (e.g. hi, hello, hey), respond politely with a short greeting
    and tell them that if they provide any email text, attachment names, or links,
    other agents will analyze it and give results such as:
      - Whether the email is PHISHING or LEGITIMATE
      - Whether attachments are SAFE, SUSPICIOUS, or DANGEROUS
      - Whether links are SAFE, SUSPICIOUS, or DANGEROUS
    Do not trigger classification, explanation, or advice steps.
    If the user provides email content, links, or attachments, pass it along to the next agents.
    """,
    model="gemini-2.0-flash"
)