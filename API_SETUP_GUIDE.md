# 🧠 Mental Healthcare Chatbot

<div align="center">

![Mental Healthcare](https://img.shields.io/badge/Mental-Healthcare-purple?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜-green?style=for-the-badge)

**Your safe space to talk, reflect, and find balance. 💙**

</div>

---

## ✨ Features

- 🤝 **Supportive Conversations** - AI-powered mental health support
- 🔒 **Private & Secure** - Your conversations stay confidential
- 🌟 **Evidence-Based** - Guidance based on mental health best practices
- 🎨 **Modern UI** - Beautiful, interactive interface with smooth animations
- 📊 **Mood Tracking** - Daily mood check-ins
- 💾 **Chat History** - Save and download your conversations
- 🎯 **Quick Starters** - Pre-built prompts for common topics

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mental-healthcare-chatbot-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys** (See detailed instructions below)
   ```bash
   # Copy the .env file and add your API keys
   # The .env file is already created - just update the keys
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🔑 API Key Configuration

### Where to Add Your API Keys

You have **TWO options** for configuring API keys:

#### Option 1: Using `.env` File (Recommended)

The `.env` file is located in the project root directory. This is the **easiest and most secure** method.

**Steps:**
1. Open `.env` file in the project root
2. Add your API key to the appropriate section
3. The app will automatically load these values

**Example:**
```env
# --- GEMINI (Google) - CURRENTLY ACTIVE ---
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL_NAME=gemini-2.0-flash-exp
```

#### Option 2: Using `.streamlit/secrets.toml`

Alternatively, you can use Streamlit's secrets management:

**Steps:**
1. Navigate to `.streamlit/secrets.toml`
2. Add your API keys there
3. The app will fall back to this if `.env` is not configured

---

### 🤖 Supported LLM Providers

The chatbot supports multiple AI providers. Choose the one that works best for you:

#### 1. **Google Gemini** (Currently Active - Recommended)

**Why Gemini?**
- ✅ Free tier available
- ✅ Fast responses
- ✅ Good at conversational AI
- ✅ Easy to set up

**How to Get Your API Key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

**Configuration in `.env`:**
```env
GEMINI_API_KEY=AIzaSy...your_key_here
GEMINI_MODEL_NAME=gemini-2.0-flash-exp
```

---

#### 2. **OpenRouter** (Alternative)

**Why OpenRouter?**
- ✅ Access to multiple models
- ✅ Pay-as-you-go pricing
- ✅ Some free models available

**How to Get Your API Key:**
1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for an account
3. Go to [API Keys](https://openrouter.ai/keys)
4. Create a new API key

**Configuration in `.env`:**
```env
OPENROUTER_API_KEY=sk-or-v1-...your_key_here
OPENROUTER_MODEL_NAME=openai/gpt-4o-mini
```

**To activate:** Change line 114 in `llm/langchain_utils.py`:
```python
language_model = get_llm(provider="openrouter")
```

---

#### 3. **Groq** (Alternative - Very Fast)

**Why Groq?**
- ✅ Extremely fast inference
- ✅ Free tier available
- ✅ Great for real-time chat

**How to Get Your API Key:**
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for an account
3. Navigate to API Keys section
4. Create a new API key

**Configuration in `.env`:**
```env
GROQ_API_KEY=gsk_...your_key_here
GROQ_MODEL_NAME=llama-3.1-70b-versatile
```

**To activate:** Change line 114 in `llm/langchain_utils.py`:
```python
language_model = get_llm(provider="groq")
```

---

#### 4. **Azure OpenAI** (Enterprise)

**Why Azure OpenAI?**
- ✅ Enterprise-grade
- ✅ Microsoft support
- ✅ Advanced features

**How to Get Your API Key:**
1. Create an Azure account
2. Set up Azure OpenAI service
3. Deploy a model
4. Get your endpoint and API key

**Configuration in `.env`:**
```env
AZURE_OAI_KEY=your_azure_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

**To activate:** Change line 114 in `llm/langchain_utils.py`:
```python
language_model = get_llm(provider="azure")
```

---

## 🎨 UI Features

### Modern Design Elements

- **Glassmorphism Effects** - Frosted glass aesthetic
- **Gradient Backgrounds** - Beautiful purple-to-violet gradients
- **Smooth Animations** - Fade-in, slide, and hover effects
- **Loading States** - Initial loading animation and thinking indicators
- **Responsive Design** - Works on desktop and mobile
- **Custom Scrollbar** - Styled to match the theme

### Interactive Elements

- **Hover Effects** - Buttons and cards respond to mouse movement
- **Transitions** - Smooth state changes
- **Mood Slider** - Visual mood tracking
- **Quick Starters** - One-click conversation starters

---

## 📁 Project Structure

```
mental-healthcare-chatbot-main/
├── app.py                      # Main application entry point
├── .env                        # Environment variables (API keys)
├── requirements.txt            # Python dependencies
├── .streamlit/
│   └── secrets.toml           # Alternative secrets storage
├── app_utils/
│   ├── streamlit_utils.py     # UI components and logic
│   └── styles.py              # CSS styling and animations
├── llm/
│   └── langchain_utils.py     # LLM provider configurations
├── db/
│   └── db_helper.py           # Vector database utilities
└── faiss_db_raptor/           # Vector embeddings storage
```

---

## 🔧 Configuration

### Switching LLM Providers

To change the AI provider:

1. **Update your `.env` file** with the new provider's API key
2. **Edit `llm/langchain_utils.py`** (line 114):
   ```python
   language_model = get_llm(provider="gemini")  # Change to: groq, openrouter, azure
   ```
3. **Restart the application**

### Customizing the UI

Edit `app_utils/styles.py` to customize:
- Colors and gradients
- Animations and transitions
- Font styles
- Layout spacing

---

## 🛠️ Troubleshooting

### Common Issues

#### 1. **Authentication Error (401)**
```
openai.AuthenticationError: Error code: 401
```
**Solution:** 
- Check that your API key is correct in `.env`
- Ensure you're using a valid, active API key
- Verify the provider is correctly set in `langchain_utils.py`

#### 2. **Module Not Found**
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution:**
```bash
pip install -r requirements.txt
```

#### 3. **FAISS Database Error**
```
Failed to load FAISS vector store
```
**Solution:**
- Ensure the `faiss_db_raptor` directory exists
- Check that embeddings are properly configured

---

## 📝 Usage Tips

### Getting the Most Out of the Chatbot

1. **Be Specific** - The more details you provide, the better the guidance
2. **Use Mood Tracking** - Regular check-ins help track your progress
3. **Save Your Chats** - Download important conversations for reflection
4. **Try Quick Starters** - Great for when you're not sure where to begin

### Important Disclaimer

⚠️ **This chatbot provides supportive guidance but is NOT a replacement for professional mental health care.**

If you're experiencing a mental health crisis:
- 🆘 Call emergency services (911 in US)
- 📞 Contact a crisis helpline
- 🏥 Visit your nearest emergency room
- 👨‍⚕️ Speak with a licensed mental health professional

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)
- AI models from Google Gemini, OpenRouter, Groq, and Azure OpenAI
- Vector embeddings from HuggingFace

---

<div align="center">

**Made with ❤️ for mental health awareness**

*Created by Sarweshwar*

</div>
