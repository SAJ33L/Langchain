"""
Task: 2 Create a graph that will pass in a single list of integers along with a name and an operation. If the operation is a
"+", you add the elements and if the operation is a "*", you multiply the elements, all within the same node.
"""

from typing import TypedDict, List
from langgraph.graph import StateGraph
from IPython.display import display, Image
import math

class AgentState(TypedDict):
    """
    Represents the state of the agent which can have multiple data types.
    """
    message: str
    operation: str
    numbers: List[int]
    result: str

def operation_node(state: AgentState) -> AgentState:
    """
    Processes the numbers in the state based on the specified operation,
    calculates the result, and updates the message.
    """
    print(state)

    if state["operation"] == "+":
        state["result"] = f"The sum of the numbers is: {sum(state['numbers'])}"
    elif state["operation"] == "*":
        state
        state["result"] = f"The average of the numbers is: {math.prod(state['numbers'])}"
    else:
        state["result"] = "Unknown operation"
    
    state["message"] = f"Operation completed the result is: {state['result']}"

    print(state)
    
    return state

graph = StateGraph(AgentState)

graph.add_node("operation_node", operation_node)
graph.set_entry_point("operation_node")
graph.set_finish_point("operation_node")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({
    "operation": "+",
    "numbers": [1, 2, 3, 4, 5]
})

print(result["message"])
print(result)