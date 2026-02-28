from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greetings")

@mcp.tool()
def greetings(name: str) -> str:
    "Send greetings"
    return f"Hello {name}, Have a nice day"

if __name__ =="__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0",port=8000)