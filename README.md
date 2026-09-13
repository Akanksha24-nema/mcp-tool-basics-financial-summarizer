# mcp-tool-basics-financial-summarizer

A simple multi-agent AI system built with the **Model Context Protocol (MCP)**, using a local open-source LLM (Mistral via Ollama). The project demonstrates how to separate data access (via an MCP tool) from reasoning (via an LLM), letting multiple agents share the same standardized data source.

## Overview

This project sets up:
- An **MCP server** that exposes a tool for reading sections of a company report.
- A **Researcher agent** that queries the MCP tool to extract raw data.
- An **Editor agent** that takes the raw data and uses a local LLM (Mistral, via Ollama) to generate a polished, business-ready summary.

## How it works

```
Local data store → MCP server (tool) → Researcher agent → Editor agent → Ollama (Mistral) → Final summary
```

1. The MCP server exposes a `read_company_report(section)` tool backed by a local data dictionary.
2. The Researcher agent calls this tool to fetch a specific section (e.g. `"ai revenue jump"`).
3. The Editor agent wraps the retrieved text into a prompt and sends it to Mistral via Ollama.
4. Ollama returns a one-sentence, professional summary, which is printed as the final output.

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed locally
- The `mistral` model pulled via Ollama

## Setup

**1. Pull the local model:**
```bash
ollama pull mistral
```

**2. Create and activate a virtual environment (recommended):**
```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

**3. Install dependencies:**
```bash
pip install mcp ollama
```

> **Note:** If you're using `mcp` version 2.x, the import path has changed from `mcp.server.fastmcp` to `mcp.server.mcpserver`, and `FastMCP` is now `MCPServer`. Either update your imports accordingly, or pin an older version with `pip install "mcp<2"`.

## Usage

Run the script:
```bash
python code1.py
```

Expected output:
```
Starting multi-agent system with MCP

Researcher is requesting data for: ai revenue jump
Researcher received the following data: AI-related revenue grew by 30% year-on-year.

Editor is now processing data received from researcher

Final output as per the editor is:
AI-related revenue increased by 30% year-on-year, reflecting strong momentum in AI-driven growth.
```

## Project structure

```
Multi_agent_using_MCP/
├── code1.py          # Main script: MCP server + multi-agent workflow
├── requirements.txt  # Python dependencies (optional)
├── .gitignore
└── README.md
```

## Key concepts

- **MCP (Model Context Protocol):** A standard that lets AI agents access external tools and data sources without custom integration code for each one.
- **Separation of concerns:** Data extraction (MCP tool) is fully decoupled from reasoning (LLM call) — any number of agents can reuse the same tool.
- **Local-first:** No paid APIs are used. All inference runs locally via Ollama.

## Future improvements

- Replace the hardcoded data store with a real data source (file, database, or API).
- Run the MCP server as a separate process and connect via a real MCP client (instead of a direct function call).
- Add more specialized agents (e.g. a Fact-Checker or Risk Analyst agent).

## License

MIT
