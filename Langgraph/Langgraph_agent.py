from langchain_ults import init_gemini_model
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool

# Initialize model
llm = init_gemini_model()

# Calculator tool
@tool
def calculator(expression: str) -> str:
    """Useful for performing mathematical calculations"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error in calculation: {str(e)}"

# Custom greeting tool
@tool
def greet(name: str) -> str:
    """Greets the user by name in a friendly way."""
    return f"Hello {name}! Welcome, hope you are having a great day!"

# Define tools list
tools = [calculator, greet]

# Create react agent using langgraph prebuilt
agent = create_react_agent(llm, tools)

# Run the agent
print("LangGraph Agent is ready! Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bye!")
        break

    response = agent.invoke({"messages": [HumanMessage(content=user_input)]})

    print("Agent:", response["messages"][-1].content)