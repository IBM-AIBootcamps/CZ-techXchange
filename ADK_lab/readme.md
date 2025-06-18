
# Watsonx Orchestrate ADK lab
Simple watsonx Orchestrate ADK demo. Follow instructions in **Watsonx Orchestrate ADK lab.pdf**.

---- 
For watsonx.ai integration use wxai_agent.py example.

For langfuse integration use:

```console
orchestrate settings observability langfuse configure \
--url "https://cloud.langfuse.com/api/public/otel" \
--api-key "sk-lf-0000-0000-0000-0000-0000" \
--health-uri "https://cloud.langfuse.com" \
--config-json '{"public_key": "pk-lf-0000-0000-0000-0000-0000"}'
```

For beeAI integration and other use external_agent.py against endpoint (e.g. in code engine) that satisfies this communication standard:

https://github.com/watson-developer-cloud/watsonx-orchestrate-developer-toolkit/tree/main/external_agent.