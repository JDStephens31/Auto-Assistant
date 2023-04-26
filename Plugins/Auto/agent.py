import os
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain import SerpAPIWrapper, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from Commands import sign_up as su
import promptGen as pg
from dotenv import load_dotenv

# Ability to access ENV files
load_dotenv()

# Setting up API Keys for Langchain
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY")
os.environ['SERPAPI_API_KEY'] = os.getenv("SERPAPI_API_KEY")

# Adds ability to search
search = SerpAPIWrapper()

# Agent Tools
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Sign Up",
        func=su.start,
        description="useful when needing to sign up for a website. The input to this tool should be the link with "
                    "'https://' at the beginning. For example, 'https://printify.com' would be the input for the link "
                    "printify.com. This tool with go to the correct link and fill in the form."
    ),
    Tool(
        name="Fill out Sign Up Form",
        func=su.get_entries,
        description="useful when filling in forms to sign up on a website. The input to this tool should be the "
                    "previous link that was opened and should have"
                    "'https://' at the beginning. For example, 'https://printify.com' would be the input for the link "
                    "printify.com."
    )
]

# Agent Response Template
template = """{agent_history} Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
{agent_scratchpad}"""

# Prompt Setup
prompt = pg.PromptTemplate(
    template=template,
    tools=tools,
    # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
    # This includes the `intermediate_steps` variable because that is needed
    input_variables=["agent_history", "input", "intermediate_steps"]
)


memory = ConversationBufferMemory(memory_key="agent_history")
output_parser = pg.OutputParser()
llm = ChatOpenAI(temperature=0)

llm_chain = LLMChain(llm=llm, prompt=prompt)
tool_names = [tool.name for tool in tools]

# Agent Initialization
agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=output_parser,
    stop=["\nObservation:"],
    allowed_tools=tool_names
)

# New agent
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)
