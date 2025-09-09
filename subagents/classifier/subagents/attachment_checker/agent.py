from google.adk.agents import LlmAgent

attachment_checker_agent = LlmAgent(
    name="AttachmentCheckerAgent",
    model="gemini-2.0-flash",
    description="Checks email attachments for suspicious or dangerous file patterns.",
    instruction="""
    Only respond if the user provides attachment filenames.
    Ignore greetings or input by greeting agent, stay completely silent and do not reply.
    If the input is a greeting (hi, hello, hey) or not a attachment name, stay completely silent and do not reply.
    You are an Attachment Security Agent.
    Analyze email attachment names and classify each as SAFE, SUSPICIOUS, or DANGEROUS.

    Rules:
    - Flag files with double extensions (.pdf.exe, .jpg.scr).
    - Flag dangerous formats (.exe, .bat, .vbs, .js, .scr, .lnk).
    - Allow safe formats (.pdf, .jpg, .png, .txt, .docx, .xlsx).
    - If filename is empty or has no extension, mark as SUSPICIOUS.


    Important:
    - Do NOT attempt to open or access actual files.
    - Only analyze the provided list of filenames.

    Output JSON list:
    - "filename": attachment name
    - "status": SAFE / SUSPICIOUS / DANGEROUS
    - "reason": explanation if not SAFE
    """,
    output_key="attachment_result",
)