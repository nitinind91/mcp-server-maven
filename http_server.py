from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greetings", host="0.0.0.0",port=8000)

@mcp.tool()
def greetings(name: str) -> str:
    "Send greetings"
    return f"Hello {name}, I say Have a nice day"

if __name__ =="__main__":
    mcp.run(transport="streamable-http")