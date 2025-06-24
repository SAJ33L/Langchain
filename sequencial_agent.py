"""
This is the third Agent the "Sequential Graph Agent"
"""


from typing import TypedDict
from langgraph.graph import StateGraph
from IPython.display import display, Image

class AgentState(TypedDict):
    """
    This is the state of my agent
    """
    name: str
    age: str
    final: str


def first_node(state: AgentState) -> AgentState:
    """
    This is node where the agent starts it's journey
    """
    state["final"] = f"Hello {state['name']}!"
    
    return state

def second_node(state: AgentState) -> AgentState:
    """
    This is node where the agent ends it's journey
    """

    state["final"] = state["final"] + f" Your age is {state['age']}!"

    return state

graph = StateGraph(AgentState)

graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"name": "Sajeel", "age": "24"})

print(result["final"])  # Output: Hello Sajeel! Your age is 24!