import os
import streamlit as st

from langchain_openai import AzureChatOpenAI
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import AzureChatOpenAI, ChatOpenAI


from langchain_community.vectorstores import FAISS

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain


def get_embeddings(provider: str = "huggingface"):
    """
    Retrieve embeddings model based on the specified provider.
    Tries to get config from environment variables first, then falls back to st.secrets.

    Args:
        provider (str): The provider for the embeddings. Defaults to 'huggingface'.

    Returns:
        Embeddings model instance.
    """
    if provider.lower() == "huggingface":
        try:
            model_name = os.getenv("EMBEDDING_MODEL_NAME") or st.secrets.get("EMBEDDING_MODEL_NAME")
            embeddings = HuggingFaceEmbeddings(
                model_name=model_name, model_kwargs={"device": "cpu"}
            )
        except Exception as e:
            st.error(f"Gemini initialization error: {e}")
            raise
    else:
        raise ValueError(f"Unsupported provider for embeddings: {provider}")

    return embeddings


def get_llm(provider: str = "gemini"):
    """
    Retrieve an LLM model based on the specified provider.
    Tries to get config from environment variables first, then falls back to st.secrets.

    Args:
        provider (str): The provider for the LLM. Defaults to 'gemini'.

    Returns:
        LLM model instance.
    """
    
    def get_config(key):
        """Helper to get config from env vars or st.secrets"""
        return os.getenv(key) or st.secrets.get(key)

    if provider.lower() == "azure":
        try:
            model = AzureChatOpenAI(
                openai_api_key=get_config("AZURE_OAI_KEY"),
                azure_endpoint=get_config("AZURE_OPENAI_ENDPOINT"),
                azure_deployment=get_config("AZURE_OPENAI_DEPLOYMENT"),
                openai_api_version=get_config("AZURE_OPENAI_API_VERSION"),
                openai_api_type="openai",
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize Azure OpenAI model: {e}")

    elif provider.lower() == "groq":
        try:
            model = ChatGroq(
                groq_api_key=get_config("GROQ_API_KEY"),
                model_name=get_config("GROQ_MODEL_NAME"),
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize Groq model: {e}")
    
    elif provider.lower() == "gemini":
        try:
            model = ChatGoogleGenerativeAI(
                model=get_config("GEMINI_MODEL_NAME"),
                google_api_key=get_config("GEMINI_API_KEY")
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize Gemini model: {e}")
        
    elif provider.lower() == "openrouter":
        try:
            # OpenRouter is OpenAI-compatible, just with a different base_url
            model = ChatOpenAI(
                api_key=get_config("OPENROUTER_API_KEY"),
                model=get_config("OPENROUTER_MODEL_NAME"),
                base_url="https://openrouter.ai/api/v1",
                # Optional: send extra parameters like reasoning
                extra_body={"reasoning": {"enabled": True}},
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize OpenRouter model: {e}")

    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    return model

def create_conversational_chain(retriever: FAISS):
    """
    Create the conversational retrieval chain.

    Args:
        retriever (FAISS): The vector database retriever.

    Returns:
        create_retrieval_chain: The conversational retrieval chain.
    """
    language_model = get_llm(provider="gemini")

    contextualize_q_system_prompt = "Given a chat history and the latest user question \
    which might reference context in the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        language_model, retriever, contextualize_q_prompt
    )

    qa_system_prompt = """You are an assistant for question-answering tasks. \
    Use the following pieces of retrieved context to answer the question. \
    If you don't know the answer, just say that you don't know. \

    {context}.
    Do not include, "According to the context" in the final output
    """

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(language_model, qa_prompt)
    conversation_chain = create_retrieval_chain(
        history_aware_retriever, question_answer_chain
    )

    return conversation_chain
