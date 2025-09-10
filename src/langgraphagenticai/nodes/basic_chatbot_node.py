from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
        Basic chatbot implementation
    """
    def __init__(self, model):
        self.llm = model

    
    def process(self, state:State):
        """
            Process the input state and generate a chatbot response.
        """
        # msg = 
        print('state: ', state)
        print('state[\'messages\']: ', state['messages'])
        return {'messages': self.llm.invoke(state['messages'])}
