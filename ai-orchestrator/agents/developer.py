from langchain_core.messages import ToolMessage

from llm import get_model
from tools.filesystem import list_files, read_file, write_file

TOOLS = [
    list_files,
    read_file,
    write_file,
]

TOOL_MAP = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
}


def developer_agent(state):

    llm = get_model("developer")
    llm_with_tools = llm.bind_tools(TOOLS)

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

=== IMPLEMENTATION RULES ===

You are an implementation agent, not a code-generation assistant.

Your job is to MODIFY THE ACTUAL PROJECT FILES.

You MUST use the filesystem tools to implement the requested change.

A change is NOT implemented until write_file has been successfully called.

Never claim that a file was created or modified unless you actually called
write_file and received a successful tool result.

Required workflow:

1. Inspect the relevant project directory using list_files.
2. Inspect relevant existing files using read_file.
3. Decide what needs to change.
4. Use write_file to create or modify the actual files.
5. Use read_file again to verify the changes.
6. Only after successful verification, provide the final summary.

IMPORTANT:
- Never describe code instead of implementing it.
- Never claim "Created" unless write_file was actually called.
- Never claim "Modified" unless write_file was actually called.
- The filesystem is the source of truth.
- Do not create a new top-level directory.
- Use the existing project structure.
- The requested implementation belongs in task-manager-core.
- Do not use paths such as core/... .
"""

    messages = [
        {
            "role": "system",
            "content": prompt,
        }
    ]

    max_iterations = 10
    changed_files = []

    for iteration in range(max_iterations):

        print(f"\n[Developer] Iteration {iteration + 1}")

        response = llm_with_tools.invoke(messages)

        messages.append(response)

        if not response.tool_calls:
            return {
                "developer_result": response.content,
                "changed_files": changed_files,
                "current_agent": "developer",
            }

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_call_id = tool_call["id"]

            print(f"\n[Developer Tool] {tool_name}")
            print(f"Arguments: {tool_args}")

            tool = TOOL_MAP.get(tool_name)

            if tool is None:
                tool_result = f"Unknown tool: {tool_name}"

            else:
                try:
                    tool_result = tool(**tool_args)

                    if tool_name == "write_file":
                        changed_files.append(tool_args["path"])

                except Exception as error:
                    tool_result = f"Tool execution failed: {error}"

            print(f"[Developer Tool Result] {tool_result}")

            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call_id,
                )
            )

    return {
        "developer_result": (
            "Developer agent stopped after reaching "
            "the maximum number of tool iterations."
        ),
        "changed_files": changed_files,
        "current_agent": "developer",
    }
