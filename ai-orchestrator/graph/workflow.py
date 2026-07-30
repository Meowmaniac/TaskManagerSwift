from langgraph.graph import StateGraph, END
from graph.state import AgentState

from agents.teacher import teacher_agent
from agents.architect import architect_agent
from agents.developer import developer_agent
from agents.reviewer import reviewer_agent
from agents.writer import writer_agent


builder = StateGraph(AgentState)

builder.add_node(
    "teacher",
    teacher_agent
)

builder.add_node(
    "architect",
    architect_agent
)

builder.add_node(
    "developer",
    developer_agent
)

builder.add_node(
    "reviewer",
    reviewer_agent
)

builder.add_node(
    "writer",
    writer_agent
)

builder.set_entry_point(
    "teacher"
)

builder.add_edge(
    "teacher",
    "architect"
)

builder.add_edge(
    "architect",
    "developer"
)

builder.add_edge(
    "developer",
    "reviewer"
)

builder.add_edge(
    "reviewer",
    "writer"
)

builder.add_edge(
    "writer",
    END
)

graph = builder.compile()