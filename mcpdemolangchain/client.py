from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["mathserver.py"],
            "transport": "stdio",
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable-http",
        },
    })
    all_tools = await client.get_tools()
    model = ChatGroq(model="llama-8b-8192")
    agent = create_react_agent(model=model, tools=all_tools)
    result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())