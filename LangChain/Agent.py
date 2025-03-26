#Creation of agent using LangChain

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_google_genai import GoogleGenerativeAI

llm_model = GoogleGenerativeAI(model = "gemini-1.5-pro", temperature = 0.7)

tools = load_tools(["wikipedia","llm-math"],llm=llm_model)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, #works like tought-action
    verbose = True #to figureout the internal steps
)
agent.run("when was elon musk born, what's his age now")
