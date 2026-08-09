from llm import get_model


def reviewer_agent(state):

    llm = get_model("reviewer")

    with open("../agents/general.md", "r", encoding="utf-8") as file:
        general_prompt = file.read()

    with open("../agents/reviewer.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""
    
{general_prompt}
{system_prompt}

=== PROJECT CONTEXT ===

{state["project_context"]}

=== ARCHITECTURE DECISION ===

{state["architect_result"]}

=== DEVELOPER IMPLEMENTATION ===

{state["developer_result"]}

=== USER REQUEST ===

{state["request"]}


Review this implementation.

"""

    response = llm.invoke(prompt)

    return {"reviewer_result": response.content, "current_agent": "reviewer"}
