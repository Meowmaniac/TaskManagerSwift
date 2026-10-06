from langchain_core.messages import ToolMessage
from langchain_core.tools import tool

from llm import get_model
from tools.filesystem import create_lesson


@tool
def save_lesson(title: str, content: str) -> str:
    """Save a completed lesson to the project's lessons folder."""
    return create_lesson(title, content)


def teacher_agent(state):

    llm = get_model("teacher")
    llm_with_tools = llm.bind_tools([save_lesson])

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

{state["roadmap"]}

=== USER REQUEST ===

{state["request"]}

Create a lesson for the user.

The lesson must be practical and connected to the current project.

After creating the lesson, use the save_lesson tool to save it
to the project's lessons folder.

Do not skip saving the lesson.
"""

    messages = [("user", prompt)]

    print("\n[Teacher] Starting lesson generation")

    for iteration in range(3):

        response = llm_with_tools.invoke(messages)

        messages.append(response)

        if not response.tool_calls:
            return {
                "teacher_result": response.content,
                "current_agent": "teacher",
            }

        for tool_call in response.tool_calls:

            print(f"\n[Teacher Tool] {tool_call['name']}")
            print(f"Arguments: {tool_call['args']}")

            if tool_call["name"] == "save_lesson":
                result = save_lesson.invoke(tool_call["args"])
            else:
                result = f"Unknown tool: {tool_call['name']}"

            print(f"[Teacher Tool Result] {result}")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"],
                )
            )

    return {
        "teacher_result": (
            "Teacher stopped after reaching the maximum " "number of tool iterations."
        ),
        "current_agent": "teacher",
    }
