from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State

from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
            Builds a basic chatbot graph using Langgraph.
            This method initializes a chatbot node using the 'BasicChatbotNode' class and integrates it into the graph. 
            The chatbot node is set as both the entry and exit point of the graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        print('BasicChatbotNode initialized')

         # Add nodes and edges to the graph
        self.graph_builder.add_node('chatbot', self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)

    def setup_graph(self, usecase):
        """
            sets up the graph for the selected usecase
        """
        print('usecase: ', usecase)
        if usecase == 'Basic Chatbot':
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()
