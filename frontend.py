import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()

SERVERS = {
    "Cloud Server": {
        "transport": "streamable_http",
        "url": "https://intellectual-plum-horse.fastmcp.app/mcp"
        
    }
}

async def main():
    client = MultiServerMCPClient(SERVERS)
    tools = await client.get_tools()
    print("Tools:", [t.name for t in tools])

if __name__ == "__main__":
    asyncio.run(main())