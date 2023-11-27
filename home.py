import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["OPENAI_API_KEY"]


st.set_page_config(
    page_title="Home",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded",
)


with st.sidebar:
    st.markdown('''
                ### Contact
                - [LinkedIn](https://www.linkedin.com/in/pastorio/)
                - [GitHub](https://github.com/Pastorio)
                ''')


def main():
    '''Main function of the App'''
    st.markdown('''
                # Project Overview: Multifunctional Chatbot System

                ## Introduction

                This application utilizes Large Language Models and LangChain to create a versatile chatbot system. The system encompasses distinct applications, each serving a unique purpose and highlighting the adaptability of the underlying technology.
                
                ## Applications

                ### 1. Customizable Chatbot

                #### Description
                A chatbot based on conversational memory retrieval. Engage in natural and context-aware conversations with the chatbot.




                ### 2. Chatbot with PDF File Integration

                #### Description
                Interact with a chatbot powered by RAG, focusing on retrieving information from PDF files. This option demonstrates the capability of using language models for specific document-related queries.


                
                ## Technologies Used

                - **Large Language Models:** The core of each application relies on advanced language models for natural language understanding and generation.
                - **LangChain:** LangChain is used for seamless integration and interaction with external data sources, such as PDF files and web pages.

                ''')
    
if __name__ == "__main__":
    main()