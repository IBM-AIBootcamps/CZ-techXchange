from ibm_watsonx_orchestrate.agent_builder.agents import (
    Agent,
    ExternalAgent,
    AgentKind,
    AgentProvider,
    ExternalAgentAuthScheme,
    AgentStyle,
)

external_deep_researcher = ExternalAgent(
    kind=AgentKind.EXTERNAL,
    name="deep_researcher",
    title="Deep Researcher",
    nickname="deep_researcher",
    provider=AgentProvider.EXT_CHAT,
    description="Does a deep research for a given topic.",
    tags=["beeai_framework"],
    api_url="https://wxo-beeai.1wqsdonsxa6q.eu-de.codeengine.appdomain.cloud/chat/completions",
    auth_scheme=ExternalAgentAuthScheme.API_KEY,
    auth_config={"token": "123"},
    chat_params={"stream": True},
    config={"hidden": False, "enable_cot": True},
    llm="ibm/granite-3-3-8b-instruct",
)

# External Agents can only be used as a collaborator of a native agent as shown below
native_agent = Agent(
    name="native_deep_researcher",
    description="Does a deep research for a given topic.",
    style=AgentStyle.DEFAULT,
    instructions="Do a deep research by delegating a task to the collaborator.",
    tools=[],
    llm="watsonx/ibm/granite-3-3-8b-instruct",
    collaborators=[external_deep_researcher],
)
