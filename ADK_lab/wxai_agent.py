from ibm_watsonx_orchestrate.agent_builder.agents import Agent, AgentKind, AgentProvider, ExternalAgentAuthScheme

main_agent = Agent(
    name="wxai_agent",
    kind=AgentKind.EXTERNAL,
    title="Watsonx.ai agent",
    nickname="wxai_agent",
    provider=AgentProvider.WATSONX,     
    description="Hlavní agent. Řídí řešení problému a odpovídá uživateli.",
    description="An agent built in langchain which searches the news.\n",
    tags=['test'],
    api_url="https://us-south.ml.cloud.ibm.com/ml/v4/deployments/<id>/ai_service_stream?version=2021-05-01",
    auth_scheme=ExternalAgentAuthScheme.API_KEY,
    auth_config={
        "token": "my-api-key"
    },
    chat_params={
        "stream": True                                      # should the external agent be invoked using using SSE streaming or as a rest call
    },
    config={
        "hidden": False,
        "enable_cot": True
    }
)