"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools import web_search
from google.adk.tools import google_search, code_execution, web_fetch

root_agent = llm_agent.Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="A helpful assistant that can answer questions.",
    instruction="""You are a helpful agent that answers questions directly and concisely.
    Follow the instructions carefully to provide the best possible answer:
    1. If the question doesn't ask for information beyond what is provided, answer directly using code_execution and go to step 6.
    2. If information not included in the question is required, search online using google_search
    3. Use web_fetch to check the content of the pages
    4. Analyze the contents of the pages using code_execution
    5. Come up with a final answer based on the information gathered
    6. Once all steps are finished and an answer is created, always make sure your answer is properly spaced and grammatically correct if a sentence answer is required. """,
    tools=[google_search, code_execution, web_fetch],
    sub_agents=[],
)
