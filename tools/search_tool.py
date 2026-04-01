from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def search(query: str) -> str:
    """Useful for searching the internet for current information. Input should be a search query."""
    try:
        search = SerpAPIWrapper()
        result = search.run(query)
        return result
    except Exception as e:
        return f"Error in search: {str(e)}"
