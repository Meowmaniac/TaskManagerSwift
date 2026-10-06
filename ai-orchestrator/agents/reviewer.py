from llm import get_model
from tools.filesystem import list_files, read_file


def reviewer_agent(state):

    llm = get_model("reviewer")

    with open("../agents/general.md", "r", encoding="utf-8") as file:
        general_prompt = file.read()

    with open("../agents/reviewer.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    changed_files = state["changed_files"]

    actual_files = {}

    for path in changed_files:
        actual_files[path] = read_file(path)

    project_structure = list_files(".")

    prompt = f"""
{general_prompt}

{system_prompt}

=== PROJECT CONTEXT ===

{state["project_context"]}

=== ARCHITECTURE DECISION ===

{state["architect_result"]}

=== PROJECT STRUCTURE ===

{project_structure}

=== DEVELOPER RESULT ===

{state["developer_result"]}

=== CHANGED FILES ===

{changed_files}

=== ACTUAL IMPLEMENTATION ===

{actual_files}

=== REVIEW TASK ===

Review the implementation made by the Developer.

The Developer Result is only a hint about what was implemented.
It is NOT the source of truth.

The following information was collected directly from the project
filesystem by the orchestrator:

- PROJECT STRUCTURE shows the actual project structure.
- CHANGED FILES shows files actually modified by the Developer.
- ACTUAL IMPLEMENTATION contains the actual contents of those files.

Use this information as the source of truth for the review.

Evaluate:

1. Whether the files were created in the correct location.
2. Whether the project structure follows the Architect's decision.
3. Whether responsibilities belong to the correct module and layer.
4. Whether duplicate or misplaced files were introduced.
5. Whether the implementation follows the intended architecture.
6. Code quality and Swift best practices.

Do not invent implementation details that are not present
in the provided project information.

Do not modify any files.

Produce the final review according to the review format
defined in reviewer.md.
"""

    print("\n[Reviewer] Starting review")

    response = llm.invoke(prompt)

    return {
        "reviewer_result": response.content,
        "current_agent": "reviewer",
    }
