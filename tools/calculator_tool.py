from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Useful for performing mathematical calculations. Input should be a math expression like '2 + 2' or '10 * 5'."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error in calculation: {str(e)}"
