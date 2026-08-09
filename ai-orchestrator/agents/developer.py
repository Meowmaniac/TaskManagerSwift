from llm import get_model


def developer_agent(state):

    llm = get_model("developer")

    with open("../agents/general.md", "r", encoding="utf-8") as file:
        general_prompt = file.read()

    with open("../agents/developer.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""
    
{general_prompt}
{system_prompt}

=== PROJECT CONTEXT ===

{state["project_context"]}

=== ARCHITECTURE DECISION ===

{state["architect_result"]}

=== USER REQUEST ===

{state["request"]}


Implement the requested feature according to the architecture.
Provide complete code examples and explain any important implementation decisions.

"""

    response = llm.invoke(prompt)

    return {"developer_result": response.content, "current_agent": "developer"}
