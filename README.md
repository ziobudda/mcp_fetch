# Web Analyzer MCP

A simple MCP (Model Context Protocol) server that analyzes web pages through Claude Desktop.

## Prerequisites

- Python 3.12 or higher
- Claude Desktop application installed

## Installation

1. Clone or create the project directory:
```bash
mkdir web_analyzer
cd web_analyzer
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate
```

3. Create the following files in your project directory:

requirements.txt:
```
mcp>=1.0.0
httpx>=0.27.0
beautifulsoup4>=4.12.0
```

web_analyzer.py: (copy the provided MCP server code)

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure Claude Desktop:
- Open or create the configuration file:
  - On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - On Windows: `%APPDATA%\Claude\claude_desktop_config.json`

- Add the following configuration (adjust paths according to your system):
```json
{
  "mcpServers": {
    "web-analyzer": {
      "command": "/full/path/to/your/venv/bin/python",
      "args": ["/full/path/to/your/web_analyzer.py"],
      "env": {}
    }
  }
}
```

6. Restart Claude Desktop

## Usage

1. Make sure your virtual environment is activated
2. Open Claude Desktop
3. Click on the 🔌 icon to verify that web-analyzer is connected
4. Ask Claude to analyze any webpage using the analyze_url tool

## Troubleshooting

If the server doesn't appear in Claude Desktop:
1. Check that all paths in claude_desktop_config.json are correct
2. Verify that the virtual environment is activated
3. Ensure all dependencies are installed
4. Check Claude Desktop logs for errors
