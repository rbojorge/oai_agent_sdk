# import os
# from dotenv import load_dotenv
from agents import Agent, Runner

# load_dotenv()

# api_key = os.environ.get("OPENAI_API_KEY")

# if not api_key:
#     raise ValueError("OPENAI_API_KEY is not set in the enviroment variables")


def hello_agent():
    hello_agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = Runner.run_sync(
        hello_agent, "Write a haiku about recursion in programming."
    )

    return result.final_output
