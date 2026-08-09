from typing import TypedDict


class AgentState(TypedDict):

    request: str

    project_context: str
    roadmap: str

    teacher_result: str
    architect_result: str
    developer_result: str
    reviewer_result: str
    technical_writer_result: str

    current_agent: str
