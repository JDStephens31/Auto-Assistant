import os
import random
from selenium import webdriver
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv

load_dotenv()

# Chrome Driver Initialization
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\jonet\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY")

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)


def savePaper(agentInput):
    inp = agentInput
    file_name = "researchData.txt"
    file_path = "Agent Workspace\\" + file_name
    f = open(file_path, "r+")
    text = f.read()
    f.truncate(0)
    number = random.randrange(1, 100)
    file_name = "paper" + str(number) + ".txt"
    file_path = "Agent Workspace\\" + file_name
    f = open(file_path, "w")
    f.write(text)
    f.close()
    osCommandString = "notepad.exe " + file_path + ""
    os.system(osCommandString)
    return "Final Answer: Paper has been added to " + file_path + "."
