import asyncio
from mcp.server.mcpserver import MCPServer
import ollama

#initializing server
mcp = MCPServer("Research Server")

#expose a tool to the agent via MCP
@mcp.tool()
def read_company_report(section: str) ->str:
    """
    Simulates reading a company's report."""
    data_store= {
        "revenue increase": "Total global revenue grew by 4.0 percent in local currency.",
        "ai revenue jump": "AI-related revenue grew by 30% year-on-year.",
        "annual investment": "EY spends US$1 billion annually to build bespoke software and code lines driven by AI agents",
        "audit transformation": "Over 160,000 audit professionals are now equipped with generative AI capabilities." ,
        "productivity shifts": "While AI accelerates task delivery, EY notes that removing repetitive work alters traditional learning curves for entry-level talent"
    }
    print("Available keys:", list(data_store.keys()))   # debug line
    print("Looking up:", repr(section.lower()))          # debug line — repr shows hidden spaces
    return data_store.get(section.lower(),"Section not found")
#2 defining multiagent workflow:
async def run_multi_agent_system():
    print("Starting multi-agent systemt with MCP")

    #AGENT 1: Researcher doing data extraction
    target_section = "ai revenue jump"
    print(f"\n Researcher is requesting data for:{target_section}")

    #USING STANDARDISED MCP TOOL TO GET CONTEXT
    raw_data = read_company_report(target_section)
    print(f"researcher recieved the following data: {raw_data}")

    #AGENT 3: The Editor()
    print("\n Editor is now processing data recieved from researcher")

    prompt= (f"You are an expert finanacial editor. Please summarize the following data for a business report: {raw_data}")

    #calling ollama API to get the summary
    response = ollama.chat(model= 'mistral', messages =[{"role":"user", "content": prompt}])

    final_output = response['message']['content']
    print(f"\n final output as per the editor is :\n{final_output}")


if __name__ == "__main__":
    asyncio.run(run_multi_agent_system())