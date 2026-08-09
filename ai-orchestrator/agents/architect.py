from llm import get_model


def architect_agent(state):

    llm = get_model("architect")

    with open("../agents/general.md", "r", encoding="utf-8") as file:
        general_prompt = file.read()

    with open("../agents/architect.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""

{general_prompt}
{system_prompt}

=== PROJECT CONTEXT ===

{state["project_context"]}

=== ROADMAP ===

{state['roadmap']}


=== USER REQUEST ===

{state["request"]}


Create architecture decision.

"""

    result = llm.invoke(prompt)

    return {"architect_result": result.content, "current_agent": "architect"}
