import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory

import streamlit as st

st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    # layout="wide",
    # initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
    st.sidebar.header('Chat Bot configuraiton')
    # API Key
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    
    # Prompt
    # user_prompt = st.text_input("Enter your prompt")  
     
    # Temperature
    # temperature = st.slider('Temperature:', 0.0, 1.0, 0.2)
    # st.write("Temperature ", temperature)



def main():
    '''Main function of the App'''

    st.header("Custom Chat")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Initialize chat model 
    if "chain_buff" not in st.session_state:
        model = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], 
                            model_name="gpt-3.5-turbo", 
                            temperature=0.3)
        
        st.session_state.chain_buff = ConversationChain(
            llm=model,
            memory=ConversationBufferMemory()
        )
            
    # Generate response for user input
    if chat_input := st.chat_input("Make a question"):
        # User input
        with st.chat_message("user"):
            st.markdown(chat_input)
            
        st.session_state.messages.append({"role": "user", "content": chat_input})
        
        # Model response
        output = st.session_state.chain_buff(chat_input)
        
        st.session_state.messages.append({"role": "assistant", "content": output['response']})
        st.chat_message("assistant").write(output['response'])
        
    # # Accept user prompt
    # if prompt_input := st.sidebar.text_input("Enter your prompt"):
    #     prompt_dict_index = next((index for index, d in enumerate(st.session_state.messages) if d['role'] == 'prompt'), None)

    #     if prompt_dict_index is None:
    #         new_prompt_dict = {'role': 'prompt', 'content': prompt_input}
    #         st.session_state.messages.insert(0, new_prompt_dict)
    #     else:
    #         st.session_state.messages[prompt_dict_index]['content'] = prompt_input
        


if __name__ == "__main__":
    main()