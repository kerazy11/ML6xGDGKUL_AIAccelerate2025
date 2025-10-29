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
    1. Check if an answer can be found with information from the question itself
    2. If more information is needed, search online using google_search
    3. Use web_fetch to check the content of the pages
    4. Analyze the contents of the pages using code_execution if necessary
    5. Provide a final answer based on the information gathered
    Make sure your answer is properly spaced and grammatically correct if a sentence answer is required. """,
    tools=[google_search, code_execution, web_fetch],
    instruction="You are a helpful agent that answers questions directly and concisely. You check if an answer can be found with information from the question itself, and if more information is needed, search online using google_search and use web_fetch to check the content of the pages. Make sure your answer is properly spaced and grammatically correct if a sentence answer is required. ",
    sub_agents=[],
)
