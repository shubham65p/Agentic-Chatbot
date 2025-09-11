from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    def __init__(self, model):
        self.llm = model


    def process(self, state: State) -> dict:
        """
            Processes the input state and generated a response with tool integration.
        """
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke([{'role': 'user', 'content': user_input}])

        # simulate tool specific logic
        tool_response = f'Tool integration for: {user_input}'

        return {'messages': [llm_response, tool_response]}
    

    def create_chatbot(self, tools):
        """
            Returns a chatbot node functions
        """

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State) -> dict:
            """
                Chatbot logic for processing the input state and returning a response.
            """
            msg = llm_with_tools.invoke(state['messages'])
            print('messs: ', msg)
            return {'messages': [msg]}
        
        return chatbot_node