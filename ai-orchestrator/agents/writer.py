from llm import get_model


def writer_agent(state):

    llm = get_model("writer")

    with open("../agents/technical_writer.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""
{system_prompt}

You are Technical Writer.

=== PROJECT CONTEXT ===

{state["project_context"]}

=== TEACHER NOTES ===

{state["teacher_result"]}

=== ARCHITECTURE DECISION ===

{state["architect_result"]}

=== DEVELOPER IMPLEMENTATION ===

{state["developer_result"]}

=== REVIEW ===

{state["reviewer_result"]}

=== USER REQUEST ===

{state["request"]}

Create project documentation based on all previous results.

"""

    response = llm.invoke(prompt)

    return {
        "writer_result": response.content,
        "current_agent": "writer"
    }