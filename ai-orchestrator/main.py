from agents.teacher import teacher_agent
from agents.architect import architect_agent
from agents.developer import developer_agent
from agents.reviewer import reviewer_agent

# from agents.technical_writer import technical_writer_agent

# Load project context and roadmap from files
with open("context/project_context.md", "r", encoding="utf-8") as file:
    project_context = file.read()

with open("context/roadmap.md", "r", encoding="utf-8") as file:
    roadmap = file.read()

agents = [
    ("teacher", teacher_agent),
    ("architect", architect_agent),
    ("developer", developer_agent),
    ("reviewer", reviewer_agent),
    # ("technical_writer", technical_writer_agent),
]

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

    try:

        for agent_name, agent_function in agents:

            while True:

                print("\n")
                print("=" * 50)
                print(agent_name.upper())
                print("=" * 50)

                result = agent_function(state)

                # Save agent result into state
                state.update(result)

                # Print only the actual result
                result_key = f"{agent_name}_result"

                print(state.get(result_key, "No result"))

                print("=" * 50)

                command = (
                    input("\n[Enter] Continue | [r] Regenerate | [q] Stop: ")
                    .strip()
                    .lower()
                )

                if command == "r":
                    print("\nRegenerating...\n")
                    continue

                if command == "q":
                    print("\nWorkflow stopped")
                    raise StopIteration

                break

    except KeyboardInterrupt:
        print("\nWorkflow interrupted")

    except StopIteration:
        continue
