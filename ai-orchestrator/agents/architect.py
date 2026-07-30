from llm import get_model

def architect_agent(state):

    llm = get_model("architect")

    with open("../agents/architect.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""

{system_prompt}

=== PROJECT CONTEXT ===

{state["project_context"]}

=== ROADMAP ===

{state['roadmap']}

=== TEACHER NOTES ===

{state["teacher_result"]}


=== USER REQUEST ===

{state["request"]}


Create architecture decision.

"""

    result = llm.invoke(prompt)


    return {
        "architect_result": result.content,
        "current_agent": "architect"
    }