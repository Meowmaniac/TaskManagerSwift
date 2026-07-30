from graph.workflow import graph

# Load project context and roadmap from files
with open("context/project_context.md", "r", encoding="utf-8") as file:
    project_context = file.read()

with open("context/roadmap.md", "r", encoding="utf-8") as file:
    roadmap = file.read()

print("=" * 60)
print("🤖 AI Learning Team")
print("=" * 60)

while True:
    request = input("\nEnter request ('exit' to quit):\n> ").strip()

    if request.lower() == "exit":
        print("\nGoodbye!")
        break

    state = {
        "request": request,
        "project_context": project_context,
        "roadmap": roadmap,
    }

    result = graph.invoke(state)

    print("\n" + "=" * 60)
    print("Workflow finished")
    print("=" * 60)

    print("\nTeacher Result:")
    print(result.get("teacher_result", "No output"))

    print("\nArchitect Result:")
    print(result.get("architect_result", "No output"))

    print("\nDeveloper Result:")
    print(result.get("developer_result", "No output"))

    print("\nReviewer Result:")
    print(result.get("reviewer_result", "No output"))

    print("\nTechnical Writer Result:")
    print(result.get("writer_result", "No output"))