"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools import web_search

root_agent = llm_agent.Agent(
    model='gemini-2.5-flash',
    name='agent',
    description="A helpful assistant that can answer questions.",
    sub_agents=[],
)
