import os
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.document_loaders import PyPDFLoader
import langchain.vectorstores as vectorstores
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

import streamlit as st

st.set_page_config(
    page_title="File Chat",
    page_icon="📖",
)

def save_file(file):
    '''Save file to tmp folder'''
    folder = 'tmp'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    file_path = f'./{folder}/{file.name}'
    with open(file_path, 'wb') as f:
        f.write(file.getvalue())
    return file_path
    
def init_qa_model(docs):
    '''Init QA model'''
    # Split file
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    all_splits = text_splitter.split_documents(docs)
    
    # Embedding to form a knowledge base
    embeddings = OpenAIEmbeddings()

    persist_directory = 'docs/chroma/'
    knowledgeBase = vectorstores.Chroma.from_documents(documents=all_splits,
                                        embedding=embeddings,
                                        persist_directory=persist_directory)
    
    # Init model
    model = ChatOpenAI(
        openai_api_key=os.environ["OPENAI_API_KEY"],
        model_name="gpt-3.5-turbo",
        temperature=0.3,
    )

    qa_chain = RetrievalQA.from_chain_type(model,
                                        retriever=knowledgeBase.as_retriever())
    
    return qa_chain

with st.sidebar:
    st.sidebar.header('Chat Bot configuraiton')
    
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    
    st.session_state.pdf_file = st.file_uploader('Upload your PDF Document', type=['pdf'], accept_multiple_files=True)
    
    if st.button('Initialize model', disabled=not st.session_state.pdf_file):
        # Model response
        docs = []
        for file in st.session_state.pdf_file:
            file_path = save_file(file)
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())
        
        st.session_state.qa_chain = init_qa_model(docs)

def main():
    '''Main function of the App'''

    st.header("File Chat")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        
    if ("pdf_file" not in st.session_state) | (st.session_state.pdf_file is None) | (len(st.session_state.pdf_file) == 0):
        st.info("Please add your file.")
    else:
        print(st.session_state.pdf_file)
        
    if ("qa_chain" not in st.session_state):
        st.info("Please init model.")
    
    # Generate response for user input
    if chat_input := st.chat_input("Make a question", disabled=not st.session_state.pdf_file):
        # User input
        with st.chat_message("user"):
            st.markdown(chat_input)
            
        st.session_state.messages.append({"role": "user", "content": chat_input})
        
        result = st.session_state.qa_chain({"query": chat_input})
        output = result['result']
        
        st.session_state.messages.append({"role": "assistant", "content": output})
        st.chat_message("assistant").write(output)
    
if __name__ == "__main__":
    main()