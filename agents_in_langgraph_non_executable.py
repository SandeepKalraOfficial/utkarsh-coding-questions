from typing import TypedDict
 
class FileState(TypedDict):
    filename: str
    extension: str
 
def filename_agent(state: FileState )->FileState:
    print("Filename agent running")
    state["filename"] = "doc_final.pdf"
    return state
 
def extension_agent(state: FileState)->FileState:
    print("Extension agent running")
    filename = state["filename"]
    state["extension"] = filename.split(".")[-1]
 
    return state
 
from langgraph.graph import StateGraph, PendingDeprecationWarning
 
graph = StateGraph(FileState)
 
graph.add_node("filename_agent", filename_agent)
graph.add_node("extension_agent", extension_agent)
 
graph.set_entry_point("filename_agent")
graph.add_edge("extension_agent", END)
 
app = graph.compile()
 
initial_state  = {}
result = app.invoke(initial_state)
 
print(result)

#rating: 3/5, Utkarsh was able to explain the flow and the 
# code but could not complete.