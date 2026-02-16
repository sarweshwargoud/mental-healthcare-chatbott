import os
from dotenv import load_dotenv

from db.db_helper import load_faiss_vector_store
from llm.langchain_utils import create_conversational_chain
from app_utils.streamlit_utils import initialize_session_state, display_chat_interface
import streamlit as st
#st.write("Loaded secrets:", list(st.secrets.keys()))

load_dotenv(override=True)

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]=" Mental HealthCare Chatbot"

@st.cache_resource
def get_chain():
    retriever = load_faiss_vector_store()
    return create_conversational_chain(retriever)

def main():
    """
    Main function to run the Streamlit application.
    """
    conversation_chain = get_chain()

    initialize_session_state()
    display_chat_interface(conversation_chain)


if __name__ == "__main__":
    main()
