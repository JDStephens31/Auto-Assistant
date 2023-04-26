import os
import random
from selenium import webdriver
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from Plugins.Auto.agent import agent_executor

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


def new_request(userInput):
    return llm_chain.run(userInput)


def write_paper(userInput):
    number = random.randrange(1, 100)
    file_name = "paper" + str(number)
    file_path = "./Assistant Files/" + file_name + ".txt"
    f = open("./Assistant Files/" + file_name + ".txt", "w+")
    f.write(llm_chain.run(userInput))
    f.close()
    osCommandString = "notepad.exe " + file_path + ""
    os.system(osCommandString)


agent_executor.run("Create an account with printify.com")
