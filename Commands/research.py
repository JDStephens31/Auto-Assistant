import os
from langchain import SerpAPIWrapper
from dotenv import load_dotenv

# Ability to access ENV files
load_dotenv()

# Setting up API Keys for Langchain
os.environ['SERPAPI_API_KEY'] = os.getenv("SERPAPI_API_KEY")

# Adds ability to search
search = SerpAPIWrapper()


def research(data):
    file_name = "researchData.txt"
    file_path = "Agent Workspace\\" + file_name
    f = open(file_path, "a")
    f.write(search.run(data))
    f.close()
    return "Gathering Data..."
