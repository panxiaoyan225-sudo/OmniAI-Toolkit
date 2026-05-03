OmniAI-Toolkit: A Comprehensive AI & Data Suite
🚀 View Autonomous Multi-Agent 

A modular AI automation suite providing specialized tools for autonomous agent orchestration, speech-to-text transcription, and multi-agent financial insights.

🚀 Features
🤖 Autonomous AI Agents (OpenClaw)
agents_infographic.html: An interactive architectural visualization of the multi-agent ecosystem.

Autonomous Multi-Agent Framework: Engineered an objective-driven system using OpenClaw where independent agents (Mei, John, Sam) execute complex tasks.


### 🤖 Autonomous AI Agents (OpenClaw)
* **agents_infographic.html**: An interactive architectural visualization of the multi-agent ecosystem.
* **Autonomous Multi-Agent Framework**: Engineered an objective-driven system using **OpenClaw** where independent agents (**Mei, John, Sam**) execute complex tasks.They are capable of performing tasks independently as well as working collaboratively within a team
* **Isolated Workspaces**: Each agent operates within a dedicated local file-system environment (e.g., `C:/Users/ADMINI.openclaw/...`) to ensure data security and process integrity.
* **API Gateway Orchestration**: Centralized routing via **OpenRouter** and **Ollama**, transitioning from simple chatbots to fully autonomous, goal-oriented systems.
* **Isolated Workspaces**: Each agent operates within a dedicated local file-system environment to ensure data security and process integrity.
* **API Gateway Orchestration**: Centralized routing via OpenRouter and Ollama, transitioning from simple chatbots to fully autonomous, goal-oriented systems.

🧬 Semantic Search & Embeddings
Local_Embeddings.py: Implements high-performance text vectorization using Sentence-Transformers (all-MiniLM-L6-v2) running entirely on local hardware.

Vector Similarity Engine: Utilizes NumPy to calculate Cosine Similarity between document embeddings, enabling semantic search capabilities without external API dependency.

Dimensionality Management: Processes text into 384-dimensional dense vectors, optimized for fast retrieval and low-latency downstream analytics.

🧠 Natural Language Processing (NLP)
NLP_Sentiment.py: Utilizes Hugging Face Transformers to perform emotional tone analysis on text data.

transformers_Text_classify.py: A tool for categorizing and classifying text into various labels using state-of-the-art LLMs.


=======
LangChain.py: Implements a modular "Chain" workflow using LangChain and Ollama (Llama 3) for custom prompt orchestration.


✈️ Travel Intelligence
Flight_Search_App.py: A specialized GenAI Agent that finds the top 3 cheapest flights for any given route and date. It provides real-time pricing and direct booking links.

🎙️ Speech & Audio Processing
ASR_Audio_Transcriber.py: Automates speech-to-text transcription using OpenAI's Whisper model.

Gtts_TextToAudio.py: Converts text into natural-sounding speech using Google Text-to-Speech (gTTS).

📈 Financial Intelligence
Stock_app.py: A Streamlit-based dashboard that uses LSTM (Long Short-Term Memory) neural networks to predict future stock prices based on historical data.

Genai_Agent.py: A modern AI Agent utilizing Gemini 2.0 Flash with function calling to provide real-time market insights and stock price retrieval via yfinance.

Stock_Trends.py: Script focused on technical analysis and trend identification.

🛠️ Technical Stack
Languages: Python, HTML/CSS

Agent Frameworks: OpenClaw, OpenRouter, Ollama

AI/ML Frameworks: PyTorch, Sentence-Transformers, TensorFlow/Keras, Hugging Face, LangChain, Google GenAI

Data & Math: NumPy, Pandas, Scikit-learn, YFinance

Deployment: Docker, Windows/WSL2, GitHub Actions
>>>>>>> 2a2e613 ( add embedding models)
