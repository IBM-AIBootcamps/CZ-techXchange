from ibm_watsonx_orchestrate.agent_builder.agents import Agent, AgentKind, AgentStyle
from ibm_watsonx_orchestrate.agent_builder.tools import *

my_agent = Agent(
    name="mortgage_advisor",
    kind=AgentKind.NATIVE,
    llm="watsonx/meta-llama/llama-3-3-70b-instruct",
    style=AgentStyle.REACT,
    description="Hypoteční poradce. Pokud má uživatel zájem o hypotéku nebo hypoteční kalkulaci.",
    instructions="Komunikuj pouze česky. Jsi hypoteční poradce, který obsluhuje hypoteční kalkulačku. Musíš od uživatele získat všechny potřebné vstupy, aby jsi mu mohl korektně odpověďet.",
    collaborators=[],
    tools=["mortgage_calculator"]  
    )