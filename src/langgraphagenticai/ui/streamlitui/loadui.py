import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI: 
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_option()

            # LLM Selection
            self.user_controls['selected_llm'] = st.selectbox('Select LLM', llm_options)

            if self.user_controls['selected_llm'] == 'Groq':
                # Model Selection
                model_options = self.config.get_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox('Select LLM', model_options)
                self.user_controls['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY'] = st.text_input("API Key", type='password')

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning('⚠️ Please enter your Groa API key to proceed')

            # Usecase selection
            self.user_controls['selected_usecase'] = st.selectbox('Select Usecase', usecase_options)

            if self.user_controls['selected_usecase'] == 'Chatbot with web':
                os.environ['TAVILY_API_KEY'] =  self.user_controls['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] =  st.text_input('Tavily API Key', type='password')

                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning('⚠️ Please enter your Tavily API key to proceed')

        return self.user_controls


