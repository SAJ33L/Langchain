from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    """
    A complex agent state that can handle multiple data types for a more sophisticated interaction.
    """
    message: str
    numbers: List[int]
    status: bool
    result: str
    