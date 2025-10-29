"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools import web_search
from google.adk.tools import google_search, code_execution

root_agent = llm_agent.Agent(
    model='gemini-2.5-flash',
    name='agent',
    description="A helpful assistant that can answer questions.",
    instruction="You are a helpful agent that answers questions directly and concisely. Try finding an answer using data from the question first, " \
    "If you aren't able to find",
    tools=[web_search, google_search, code_execution],
    sub_agents=[],
)
