# OmniAI-Toolkit: A Comprehensive AI & Data Suite

A modular AI automation suite providing specialized tools for stock market forecasting, speech-to-text transcription, and multi-agent financial insights.

---

## 🚀 Features


### 🧠 Natural Language Processing (NLP)
* **NLP_Sentiment.py**: Utilizes Hugging Face **Transformers** to perform emotional tone analysis on text data.
* **transformers_Text_classify.py**: A tool for categorizing and classifying text into various labels using state-of-the-art LLMs.
* **LangChain.py**: Implements a modular "Chain" workflow using **LangChain** and **Ollama** (Llama 3) for custom prompt orchestration.

### 📈 Financial Intelligence
* **Stock_app.py**: A Streamlit-based dashboard that uses **LSTM (Long Short-Term Memory)** neural networks to predict future stock prices based on historical data.
* **Genai_Agent.py**: A modern AI Agent utilizing **Gemini 2.0 Flash** with function calling to provide real-time market insights and stock price retrieval via `yfinance`.
* **Stock_Trends.py**: Script focused on technical analysis and trend identification.

### ✈️ Travel Intelligence
* **Flight_Search_App.py**: A specialized **GenAI Agent** that finds the **top 3 cheapest flights** for any given route and date. It provides real-time pricing and **direct booking links** by orchestrating calls to the FlightAPI.io database.

### 🎙️ Speech & Audio Processing
* **ASR_Audio_Transcriber.py**: Automates speech-to-text transcription using OpenAI's **Whisper** model.
* **Gtts_TextToAudio.py**: Converts text into natural-sounding speech using Google Text-to-Speech (gTTS).

---

## 🛠️ Technical Stack
- **Languages**: Python
- **AI Frameworks**: TensorFlow/Keras, Hugging Face Transformers, LangChain, Google GenAI
- **Data & APIs**: Pandas, YFinance, **FlightAPI.io**, Scikit-learn
- **Frontend**: Streamlit
- **Deployment**: Docker, Google Cloud Run

---