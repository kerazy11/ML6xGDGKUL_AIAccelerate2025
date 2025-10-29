"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools import web_search
from google.adk.tools import google_search, code_execution
from my_agent.tools import check_words

root_agent = llm_agent.Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="A helpful assistant that can answer questions.",
    instruction="You are a helpful agent that answers questions directly and concisely. You check if an answer can be found with information from the question itself, and if more information is needed, search online. Make sure your answer is properly spaced and grammatically correct if a sentence answer is required. ",
    tools=[web_search.web_search, google_search.google_search, check_words.check_words, code_execution],
    sub_agents=[],
)

language_agent = llm_agent.Agent(
    model='gemini-2.5-flash',
    name='language_agent',
    description="A helpful assistant that checks the language of the answer.",
    instruction="You are a helpful agent that ensures the answers provided are grammatically correct and well-structured. When given a sentence, you will rewrite it to improve grammar and clarity.",
    tools=[google_search.google_search]
)
