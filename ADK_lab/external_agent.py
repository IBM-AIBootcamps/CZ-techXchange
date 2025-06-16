from ibm_watsonx_orchestrate.agent_builder.agents import Agent, ExternalAgent, AgentKind, AgentProvider, ExternalAgentAuthScheme

# External Agents can only be used as a collaborator of a native agent
my_agent = ExternalAgent(
    kind=AgentKind.EXTERNAL,
    name="news_agent",
    title="News Agent",
    nickname="news_agent",
    provider=AgentProvider.EXT_CHAT,
    description="An agent built in langchain which searches the news.\n",
    tags=['test'],
    api_url="https://someurl.com",
    auth_scheme=ExternalAgentAuthScheme.BEARER_TOKEN,
    auth_config={
        "token": "123"
    },
    chat_params={
        "stream": True
    },
    config={
        "hidden": False,
        "enable_cot": True
    }
)