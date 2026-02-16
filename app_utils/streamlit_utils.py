import streamlit as st
import time
from langchain.chains import create_retrieval_chain
from langchain_core.messages import HumanMessage
from app_utils.styles import get_custom_css

def initialize_session_state():
    """
    Initialize session state variables for chat history and messages.
    """
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    if "chat_started" not in st.session_state:
        st.session_state["chat_started"] = False
    
    if "show_loading" not in st.session_state:
        st.session_state["show_loading"] = True

def get_chat_history_text():
    """Convert chat history to a formatted string for download."""
    history_text = "=== Mental Healthcare Chatbot - Chat History ===\n\n"
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        history_text += f"{role}: {msg['content']}\n\n"
        history_text += "-" * 50 + "\n\n"
    return history_text

def stream_text(text):
    """Generator function to simulate streaming text."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

def show_initial_loading():
    """Display an initial loading animation when the app starts."""
    if st.session_state.get("show_loading", True):
        loading_container = st.empty()
        
        with loading_container.container():
            st.markdown("""
                <div style="text-align: center; padding: 100px 20px;">
                    <h1 style="font-size: 3rem; background: linear-gradient(135deg, #ffffff 0%, #a8edea 100%); 
                               -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                               font-family: 'Poppins', sans-serif; animation: fadeInDown 1s ease-out;">
                        🧠 Mental Healthcare Chatbot
                    </h1>
                    <p style="font-size: 1.2rem; color: rgba(255,255,255,0.8); margin-top: 20px; animation: fadeIn 1.5s ease-out;">
                        Initializing your safe space...
                    </p>
                    <div style="margin-top: 40px;">
                        <div style="width: 60px; height: 60px; margin: 0 auto; border: 5px solid rgba(255,255,255,0.3); 
                                    border-top: 5px solid #ffffff; border-radius: 50%; animation: spin 1s linear infinite;">
                        </div>
                    </div>
                </div>
                <style>
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                </style>
            """, unsafe_allow_html=True)
        
        time.sleep(2)  # Show loading for 2 seconds
        loading_container.empty()
        st.session_state["show_loading"] = False
        st.rerun()

def handle_user_query(get_conversation_chain: create_retrieval_chain, user_query: str):
    """
    Handle the user query and get the response from the conversation chain.
    """
    # Create a placeholder for the thinking animation
    thinking_placeholder = st.empty()
    
    with thinking_placeholder.container():
        st.markdown("""
            <div style="text-align: center; padding: 20px;">
                <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; animation: pulse 1.5s ease-in-out infinite;">
                    🤔 Thinking deeply about your message...
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Get the response
    response = get_conversation_chain.invoke(
        {"input": user_query, "chat_history": st.session_state["chat_history"]}
    )
    
    # Clear the thinking animation
    thinking_placeholder.empty()

    st.session_state["chat_history"].extend(
        [HumanMessage(content=user_query), response["answer"]]
    )

    return response["answer"]

def display_landing_page():
    """Display the welcoming landing page with animations."""
    st.markdown('<h1 class="main-title">🧠 Mental Healthcare Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Your safe space to talk, reflect, and find balance. 💙</p>', unsafe_allow_html=True)

    # Add some breathing space
    st.markdown("<br>", unsafe_allow_html=True)

    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 20px; 
                        border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.2);
                        transition: all 0.3s ease; animation: fadeIn 0.8s ease-out;">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">🤝</div>
                <h3 style="color: #ffffff; font-size: 1.1rem; margin-bottom: 10px;">Supportive</h3>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Always here to listen</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 20px; 
                        border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.2);
                        transition: all 0.3s ease; animation: fadeIn 1s ease-out;">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">🔒</div>
                <h3 style="color: #ffffff; font-size: 1.1rem; margin-bottom: 10px;">Private</h3>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Your conversations are safe</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 20px; 
                        border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.2);
                        transition: all 0.3s ease; animation: fadeIn 1.2s ease-out;">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">🌟</div>
                <h3 style="color: #ffffff; font-size: 1.1rem; margin-bottom: 10px;">Helpful</h3>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Evidence-based guidance</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Main CTA button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start My Check-In", use_container_width=True, key="main_cta"):
            st.session_state["chat_started"] = True
            st.rerun()

    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: rgba(255,255,255,0.9); font-family: Poppins; animation: fadeIn 1.4s ease-out;'>Or start with a topic:</h3>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    scol1, scol2, scol3 = st.columns(3)
    
    # Helper to start chat with a prompt
    def start_with_prompt(prompt):
        st.session_state["chat_started"] = True
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    with scol1:
        if st.button("😟 Feeling Overwhelmed", key="starter_1", use_container_width=True):
            start_with_prompt("I'm feeling overwhelmed and need some guidance")
    with scol2:
        if st.button("🧘 Practice Mindfulness", key="starter_2", use_container_width=True):
            start_with_prompt("How can I practice mindfulness in my daily life?")
    with scol3:
        if st.button("🛑 Anxiety Tips", key="starter_3", use_container_width=True):
            start_with_prompt("Can you give me some tips to handle anxiety?")

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; color: rgba(255,255,255,0.6); font-size: 0.85rem; animation: fadeIn 2s ease-out;">
            <p>💡 Remember: This chatbot provides supportive guidance but is not a replacement for professional mental health care.</p>
        </div>
    """, unsafe_allow_html=True)

def display_chat_interface(conversation_chain: create_retrieval_chain):
    """
    Display the chat interface using Streamlit.
    """
    # Apply Custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)

    # Show initial loading animation
    if st.session_state.get("show_loading", True):
        show_initial_loading()
        return

    # Sidebar for Mood Check & Tools
    with st.sidebar:
        st.markdown("""
            <h2 style="color: #ffffff; font-family: 'Poppins', sans-serif; text-align: center; margin-bottom: 20px;">
                📊 Daily Mood Check-In
            </h2>
        """, unsafe_allow_html=True)
        
        mood = st.select_slider(
            "How are you feeling right now?",
            options=["😔 Very Low", "😟 Low", "😐 Neutral", "🙂 Good", "😁 Great"],
            value="😐 Neutral",
            label_visibility="collapsed"
        )
        
        st.markdown(f"""
            <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.1); 
                        border-radius: 10px; margin-top: 10px; backdrop-filter: blur(10px);">
                <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 1.1rem;">
                    Current Mood: <strong>{mood}</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
            <h3 style="color: #ffffff; font-family: 'Poppins', sans-serif; text-align: center; margin-bottom: 20px;">
                🛠️ Session Tools
            </h3>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.session_state.chat_started = False
            st.session_state.show_loading = False
            st.rerun()
            
        st.download_button(
            label="📥 Save Chat History",
            data=get_chat_history_text(),
            file_name=f"mental_health_chat_{int(time.time())}.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.markdown("---")
        
        # Quick tips section
        st.markdown("""
            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; backdrop-filter: blur(10px);">
                <h4 style="color: #ffffff; margin-bottom: 10px;">💡 Quick Tips</h4>
                <ul style="color: rgba(255,255,255,0.8); font-size: 0.85rem; line-height: 1.6;">
                    <li>Take deep breaths</li>
                    <li>Stay hydrated</li>
                    <li>Practice gratitude</li>
                    <li>Connect with others</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Main Logic
    if not st.session_state["chat_started"]:
        display_landing_page()
    else:
        # Chat Header
        st.markdown('<h2 class="chat-header">💬 Mental HealthCare ChatBot</h2>', unsafe_allow_html=True)
        
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"], avatar="🧑" if message["role"] == "user" else "🤖"):
                st.markdown(message["content"])

        # React to user input
        if user_query := st.chat_input("Share your thoughts... 💭"):
            # Display user message in chat message container
            st.chat_message("user", avatar="🧑").markdown(user_query)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_query})

            response_text = handle_user_query(conversation_chain, user_query)

            # Display assistant response with streaming effect
            with st.chat_message("assistant", avatar="🤖"):
                st.write_stream(stream_text(response_text))
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_text})
