from llm import get_model


def teacher_agent(state):

    llm = get_model("teacher")

    with open("../agents/general.md", "r", encoding="utf-8") as file:
        general_prompt = file.read()

    with open("../agents/teacher.md", "r", encoding="utf-8") as file:
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

Create a lesson.

"""

    response = llm.invoke(prompt)

    return {"teacher_result": response.content, "current_agent": "teacher"}
