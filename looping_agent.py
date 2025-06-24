"""
This is the fifth Agent the "Looping Agent"
"""

import random
from typing import TypedDict
from IPython.display import display, Image
from langgraph.graph import StateGraph, END, START

class AgentState(TypedDict):
    name: str
    number: list[int]
    counter: int

def greeting_node(state: AgentState) -> AgentState:
    """
    This is a greeting node which says hi to the person
    """
    state['name'] = input("What is your name?")
    state['name'] = f"Hi there {state['name']}!"
    state['counter'] = 0
    
    return state

def random_node(state: AgentState) -> AgentState:
    """
    Generates a random number from 0 to 10
    """
    state['number'].append(random.randint(0, 10))
    state['counter'] += 1

    return state

def should_continue(state: AgentState) -> AgentState:
    """
    Function that decides what todo next
    """

    if state['counter'] < 5:
        print("Entering Loop again ", state['counter'])
        return "loop"
    else:
        return "exit"
    
graph = StateGraph(AgentState)
graph.add_node("greeting_node", greeting_node)
graph.add_node("random_node", random_node)
graph.add_edge("greeting_node", "random_node")
graph.add_conditional_edges("random_node", should_continue,
                            {
                                "loop": "random_node",
                                "exit": END
                            })

graph.add_edge(START, "greeting_node")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke()
print(result)

