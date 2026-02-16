
def get_custom_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;600;700&display=swap');

        /* ============================================
           GLOBAL STYLES & ANIMATIONS
        ============================================ */
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-attachment: fixed;
            color: #FFFFFF;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* ============================================
           KEYFRAME ANIMATIONS
        ============================================ */
        
        @keyframes fadeIn {
            from { 
                opacity: 0; 
                transform: translateY(20px); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0); 
            }
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        @keyframes shimmer {
            0% {
                background-position: -1000px 0;
            }
            100% {
                background-position: 1000px 0;
            }
        }

        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        /* ============================================
           GLASSMORPHISM CONTAINERS
        ============================================ */
        
        .glass-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            padding: 30px;
            animation: fadeIn 0.8s ease-out;
        }

        /* ============================================
           MAIN TITLE & HEADINGS
        ============================================ */
        
        .main-title {
            text-align: center;
            background: linear-gradient(135deg, #ffffff 0%, #a8edea 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            font-size: 3.5rem;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease-out;
            text-shadow: 0 0 30px rgba(255, 255, 255, 0.3);
            font-family: 'Poppins', sans-serif;
            letter-spacing: -1px;
        }
        
        .sub-title {
            text-align: center;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 400;
            font-size: 1.3rem;
            margin-bottom: 40px;
            animation: fadeInDown 1.2s ease-out;
            font-family: 'Inter', sans-serif;
        }

        .chat-header {
            text-align: center;
            background: linear-gradient(135deg, #ffffff 0%, #ffeaa7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            font-size: 2.2rem;
            margin-bottom: 30px;
            animation: fadeInDown 0.8s ease-out;
            font-family: 'Poppins', sans-serif;
        }

        /* ============================================
           BUTTONS - PRIMARY & SECONDARY
        ============================================ */
        
        div.stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 30px;
            padding: 16px 32px;
            border: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            position: relative;
            overflow: hidden;
            font-family: 'Inter', sans-serif;
        }

        div.stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }

        div.stButton > button:hover::before {
            left: 100%;
        }

        div.stButton > button:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }

        div.stButton > button:active {
            transform: translateY(-2px) scale(1.02);
        }

        /* Starter Prompt Buttons */
        [data-testid="column"] div.stButton > button {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            color: #ffffff;
            border: 2px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            font-size: 0.95rem;
            padding: 14px 24px;
        }

        [data-testid="column"] div.stButton > button:hover {
            background: rgba(255, 255, 255, 0.25);
            border-color: rgba(255, 255, 255, 0.5);
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.3);
        }

        /* ============================================
           CHAT INPUT & MESSAGES
        ============================================ */
        
        .stChatInput {
            border-radius: 25px;
            animation: fadeIn 0.6s ease-out;
        }

        .stChatInput > div {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 25px;
            transition: all 0.3s ease;
        }

        .stChatInput > div:focus-within {
            border-color: rgba(255, 255, 255, 0.5);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
            transform: scale(1.02);
        }

        /* Chat Messages */
        .stChatMessage {
            animation: slideInLeft 0.5s ease-out;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
        }

        .stChatMessage:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        [data-testid="stChatMessageContent"] {
            color: #ffffff;
        }

        /* ============================================
           SIDEBAR STYLING
        ============================================ */
        
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(102, 126, 234, 0.3) 0%, rgba(118, 75, 162, 0.3) 100%);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.2);
        }

        section[data-testid="stSidebar"] > div {
            background: transparent;
        }

        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            color: #ffffff;
            font-family: 'Poppins', sans-serif;
            animation: fadeInDown 0.8s ease-out;
        }

        section[data-testid="stSidebar"] .stMarkdown {
            color: rgba(255, 255, 255, 0.9);
        }

        /* Mood Slider */
        .stSlider {
            animation: fadeIn 1s ease-out;
        }

        /* ============================================
           LOADING & SPINNER
        ============================================ */
        
        .stSpinner > div {
            border-top-color: #ffffff !important;
            animation: pulse 1.5s ease-in-out infinite;
        }

        /* ============================================
           DIVIDER
        ============================================ */
        
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            margin: 30px 0;
        }

        /* ============================================
           DOWNLOAD BUTTON
        ============================================ */
        
        .stDownloadButton > button {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            border-radius: 25px;
            padding: 12px 24px;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(17, 153, 142, 0.3);
        }

        .stDownloadButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 25px rgba(17, 153, 142, 0.5);
            background: linear-gradient(135deg, #38ef7d 0%, #11998e 100%);
        }

        /* ============================================
           SELECT SLIDER (MOOD)
        ============================================ */
        
        .stSelectSlider {
            animation: fadeIn 1.2s ease-out;
        }

        /* ============================================
           RESPONSIVE DESIGN
        ============================================ */
        
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            
            .sub-title {
                font-size: 1.1rem;
            }
            
            div.stButton > button {
                padding: 12px 24px;
                font-size: 1rem;
            }
        }

        /* ============================================
           CUSTOM SCROLLBAR
        ============================================ */
        
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.5);
        }

        /* ============================================
           ADDITIONAL ENHANCEMENTS
        ============================================ */
        
        /* Fade in all markdown content */
        .stMarkdown {
            animation: fadeIn 0.6s ease-out;
        }

        /* Column animations */
        [data-testid="column"] {
            animation: fadeIn 0.8s ease-out;
        }

        /* Add glow effect to important elements */
        .glow {
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
        }

    </style>
    """
