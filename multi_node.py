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
    state["name"] = input("What is your Name?")
    
    return state

def second_node(state: AgentState) -> AgentState:
    """
    This is node where the agent ends it's journey
    """
    state["age"] = input("What is your Age?")

    return state

def third_node(state: AgentState) -> AgentState:
    """
    This is node where the agent ends it's journey
    """
    state["final"] =  f"""
        Your name is {state['name']}! your age is {state['age']}. 
        Your are learning fast and doing greate work!!! KUDO to you!!!!
        """

    return state

graph = StateGraph(AgentState)

graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node")
graph.set_finish_point("third_node")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({})

print(result["final"])  # Output: Hello Sajeel! Your age is 24!