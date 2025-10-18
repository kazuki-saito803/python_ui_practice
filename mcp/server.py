from fastmcp import FastMCP


mcp = FastMCP('sample server')

@mcp.tool()
def function():
    pass