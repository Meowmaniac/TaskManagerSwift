from llm import get_model


def technical_writer_agent(state):

    llm = get_model("technical_writer")

    with open("../agents/general.md", "r", encoding="utf-8") as file:
        general_prompt = file.read()

    with open("../agents/technical_writer.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    prompt = f"""

{general_prompt}
{system_prompt}

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
        "technical_writer_result": response.content,
        "current_agent": "technical_writer",
    }
