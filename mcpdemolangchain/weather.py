from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather")

@mcp.tool()
async def get_weather(city:str)->str:
    """Get weather of a city"""
    return f"Weather of {city} is sunny"

if __name__=='__main__':
    mcp.run(transport="streamable-http")