import os
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY")

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)


def compilePaper(agentInput):
    inp = agentInput
    file_name = "researchData.txt"
    file_path = "Agent Workspace\\" + file_name
    f = open(file_path, "r+")
    text = f.read()
    fixedPaper = llm_chain.run("Turn this data into a research paper fixing any grammatical errors and removing any "
                               "sentence that is not finished: " + text)
    f.write(fixedPaper)
    f.close()
    return "Compiling Data and Fixing Errors..."
