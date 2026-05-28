def calculator(expression: str):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {str(e)}"


def search_tool(query: str):
    return f"Search results for '{query}'"

# 🔥 Tool registry (NEW)
TOOLS = {
    "calculator": calculator,
    "search_tool": search_tool
}