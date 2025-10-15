import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
from my_agents import a_hello_world

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the enviroment variables")


def main():
    print(a_hello_world.hello_agent())


if __name__ == "__main__":
    main()
