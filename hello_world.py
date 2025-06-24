"""
This is the first Agent the "Hello World Agent"
"""

from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import display, Image

class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """
    A node that returns a greeting message.
    """
    state['message'] = "Hey " + state['message'] + " how are you?"
    return state

graph = StateGraph(AgentState)
graph.add_node("greeting", greeting_node)

graph.set_entry_point("greeting")
graph.set_finish_point("greeting")

app = graph.compile()


display(Image(app.get_graph().draw_mermaid_png()))
#print(app.get_graph().draw_ascii())


result = app.invoke({"message": "Sajeel"})

print(result["message"])
