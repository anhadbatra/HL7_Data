from mcp import FastMCP

mcp = FastMCP("The first server")

@mcp.tool()
def get_lambda():
    pass