from llm import get_model


def teacher_agent(state):

    llm = get_model("teacher")

    with open("../agents/teacher.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""

You are Teacher.

=== PROJECT CONTEXT ===

{state["project_context"]}

=== ROADMAP ===

{state['roadmap']}

=== USER REQUEST ===

{state["request"]}

Create a lesson.

"""

    response = llm.invoke(prompt)

    return {
        "teacher_result": response.content,
        "current_agent": "teacher"
    }