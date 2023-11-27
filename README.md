# llm-apps

## Large Language Model Applications Repository

This collection showcases various applications powered by Large Language Models (LLMs). These applications demonstrate fundamental concepts in LLMs, including basic chat conversations, chat conversation memory, and retrieval-augmented generation (RAG) applications. Additionally, the repository includes a Streamlit application with two interactive options: a chatbot based on memory retrieval and a chatbot based on RAG using PDF files.

### Notebooks

#### `langchain_concepts.ipynb`

Explore the fundamental concepts of the LangChain library, which includes basic chat conversations, conversational memory, and RAG applications. This notebook serves as a comprehensive guide to understanding and implementing key features.

#### `rag_llama2.ipynb`

Dive into a specific application of RAG using local GPU resources with the llama2 model. This notebook provides practical insights into leveraging RAG for your specific use case.

### Pages

#### `home.py`

The main application file that hosts a Streamlit application with two options:

1. **Chatbot:**
   - A chatbot based on conversational memory retrieval. Engage in natural and context-aware conversations with the chatbot.

2. **File Chat:**
   - Interact with a chatbot powered by RAG, focusing on retrieving information from PDF files. This option demonstrates the capability of using language models for specific document-related queries.

### Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/llm-apps.git
   ```

2. Navigate to the repository:

   ```bash
   cd llm-apps
   ```

3. Set up a virtual environment using Poetry:

   ```bash
   poetry install
   ```

4. Activate the virtual environment:

   ```bash
   poetry shell
   ```

5. Run the Streamlit application:

   ```bash
   streamlit run Home.py
   ```

Now you can access the Streamlit application locally and explore the different language model applications provided in the repository.

### Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency management. The `pyproject.toml` file includes the required dependencies. 

If you don't have Poetry installed, you can install it by following the instructions on the Poetry website.