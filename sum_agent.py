"""
Second example in the video
"""

from typing import TypedDict, List
from langgraph.graph import StateGraph
from IPython.display import display, Image

class AgentState(TypedDict):
    """
    Represents the state of the agent which can have multiple data types.
    """
    numbers: List[int]
    name: str
    result: str

def process_values(state: AgentState) -> AgentState:
    """
    Processes the numbers in the state, calculates their sum, and updates the message.
    """
    print(state)
    state["result"] = f"{state['name']}, the sum of the number is: {sum(state['numbers']) }"
    print(state)
    
    return state

graph = StateGraph(AgentState)

graph.add_node("process_values", process_values)
graph.set_entry_point("process_values")
graph.set_finish_point("process_values")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({
    "numbers": [1, 2, 3, 4, 5],
    "name": "Sajeel"
})

print(result["result"])  # Output: Sajeel, the sum of the number is: 15

    