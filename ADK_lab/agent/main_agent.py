from ibm_watsonx_orchestrate.agent_builder.agents import Agent, AgentKind, AgentStyle
from ibm_watsonx_orchestrate.agent_builder.tools import *

main_agent = Agent(
    name="main_agent",
    title="Main agent",
    nickname="main_agent",
    kind=AgentKind.NATIVE,
    llm="watsonx/meta-llama/llama-3-3-70b-instruct",
    style=AgentStyle.REACT,
    description="Hlavní agent. Řídí řešení problému a odpovídá uživateli.",
    instructions="Komunikuj pouze česky. Odpovídej uživateli na všechny jeho dotazy. Pokud nebudeš znát odpověď, použij některý ze svých nástrojů.",
    collaborators=["mortgage_advisor"],
    tools=["wiki_search"],
)
