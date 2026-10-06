from pathlib import Path

# Project root is resolved relative to this file.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
print(f"[Filesystem] PROJECT_ROOT = {PROJECT_ROOT}")


def resolve_workspace_path(path: str) -> Path:
    """Resolve a path and ensure it stays inside the workspace."""

    resolved = (PROJECT_ROOT / path).resolve()

    try:
        resolved.relative_to(PROJECT_ROOT)
    except ValueError:
        raise ValueError(f"Path is outside project root: {path}")

    return resolved


def list_files(path: str = ".") -> str:
    """List files and directories inside the workspace."""

    directory = resolve_workspace_path(path)

    if not directory.exists():
        return f"Path does not exist: {path}"

    if not directory.is_dir():
        return f"Path is not a directory: {path}"

    entries = sorted(directory.iterdir())

    if not entries:
        return "(empty)"

    result = []

    for entry in entries:
        prefix = "[DIR]" if entry.is_dir() else "[FILE]"
        result.append(f"{prefix} {entry.relative_to(PROJECT_ROOT)}")

    return "\n".join(result)


def read_file(path: str) -> str:
    """Read a UTF-8 text file from the workspace."""

    file_path = resolve_workspace_path(path)

    if not file_path.exists():
        return f"File does not exist: {path}"

    if not file_path.is_file():
        return f"Not a file: {path}"

    return file_path.read_text(encoding="utf-8")


def write_file(path: str, content: str) -> str:
    """Create or overwrite a UTF-8 text file inside the workspace."""

    file_path = resolve_workspace_path(path)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")

    return f"Successfully wrote {file_path.relative_to(PROJECT_ROOT)}"


def create_lesson(title: str, content: str) -> str:
    lessons_dir = Path(__file__).resolve().parents[2] / "handbook"
    lessons_dir.mkdir(parents=True, exist_ok=True)

    existing_lessons = list(lessons_dir.glob("*.md"))
    lesson_number = len(existing_lessons) + 1

    safe_title = "".join(
        char.lower() if char.isalnum() else "_" for char in title
    ).strip("_")

    filename = f"{lesson_number:03d}_{safe_title}.md"
    lesson_path = lessons_dir / filename

    lesson_path.write_text(content, encoding="utf-8")

    return f"Lesson created: {lesson_path.relative_to(PROJECT_ROOT)}"
