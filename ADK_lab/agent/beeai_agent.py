from ibm_watsonx_orchestrate.agent_builder.agents import (
    Agent,
    ExternalAgent,
    AgentKind,
    AgentProvider,
    ExternalAgentAuthScheme,
    AgentStyle,
)

external_trip_planner_agent = ExternalAgent(
    kind=AgentKind.EXTERNAL,
    name="trip_planner",
    title="Trip Planner",
    nickname="trip_planner",
    provider=AgentProvider.EXT_CHAT,
    description="Plan activities for a given destination based on current weather and events.",
    tools=[],
    style=AgentStyle.REACT,
    instructions="You are a trip planner agent. Use your tools to find the best activities for the user based on their destination and current weather.",
    tags=["beeai_framework"],
    display_name="Trip Planner Agent",
    api_url="https://wxo-beeai.1wqsdonsxa6q.eu-de.codeengine.appdomain.cloud/chat/completions",
    auth_scheme=ExternalAgentAuthScheme.NONE,
    auth_config={},
    chat_params={"stream": True},
    config={"hidden": False, "enable_cot": True},
    llm="watsonx/meta-llama/llama-3-3-70b-instruct",
)


# External Agents can only be used as a collaborator of a native agent as shown below
native_agent = Agent(
    name="native_trip_planner",
    description="Plan activities for a given destination based on current weather and events.",
    style=AgentStyle.DEFAULT,
    instructions="Plan activities by using your collaborator.",
    tools=[],
    llm="watsonx/meta-llama/llama-3-3-70b-instruct",
    # omitted for brevity
    collaborators=[external_trip_planner_agent],
)
