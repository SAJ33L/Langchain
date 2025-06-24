"""
Task: 1 create a "Personalised Compliment Agent" using LangGraph!
"""

from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import display, Image

class AgentState(TypedDict):
    """
    This is the state of my agent
    """
    message: str

def compliment_node(state: AgentState) -> AgentState:
    """
    THis node compliments the user and maintains the state
    """
    state["message"] = f"Hey {state["message"]} you have done a great work so far, love your work!!"
    return state

graph = StateGraph(AgentState)
graph.add_node("compliment", compliment_node)
graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

compliment = app.invoke({"message": "Sajeel"})