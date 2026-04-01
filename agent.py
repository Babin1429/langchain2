from langchain_ults import init_gemini_model
from langchain_core.messages import HumanMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from tools.calculator_tool import calculator
from tools.weather_tool import weather
from tools.search_tool import search

# Initialize model
llm = init_gemini_model()

# Define all tools
tools = [calculator, weather, search]

# Create prompt template for the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use the tools available to answer the user's question."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])


agent = create_tool_calling_agent(llm, tools, prompt)

# Create agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent
user_input = input("Ask the agent anything: ")
response = agent_executor.invoke({"input": user_input})

print("\nAgent output:\n", response["output"])
