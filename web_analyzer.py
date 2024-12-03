#!/usr/bin/env python

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import httpx
from bs4 import BeautifulSoup

app = Server("web-analyzer")

async def fetch_and_analyze(url: str) -> dict:
    """Fetch and analyze a webpage."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return {
            "title": soup.title.string if soup.title else None,
            "links": len(soup.find_all("a", href=True)),
            "paragraphs": len(soup.find_all("p")),
            "images": len(soup.find_all("img"))
        }

@app.list_tools()
async def list_tools() -> list[Tool]:
    """Define available tools."""
    return [
        Tool(
            name="analyze_url",
            description="Analyze a webpage from given URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to analyze"
                    }
                },
                "required": ["url"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name != "analyze_url":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        analysis = await fetch_and_analyze(arguments["url"])
        return [TextContent(type="text", text=str(analysis))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream, 
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
