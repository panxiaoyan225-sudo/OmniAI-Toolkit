# OmniAI-Toolkit: A Comprehensive AI & Data Suite

[🚀 View Autonomous Multi-Agent Interactive Infographic](https://panxiaoyan225-sudo.github.io/panxiaoyan225-sudo/agents_infographic.html)

A modular AI automation suite providing specialized tools for autonomous agent orchestration, semantic search, financial intelligence, and speech processing.

---

## 🚀 Key Modules

### 🤖 Autonomous AI Agents (OpenClaw)
*   **Autonomous Multi-Agent Framework**: An objective-driven system utilizing **OpenClaw** where independent agents (**Mei, John, Sam**) execute complex tasks through collaborative or independent workflows.
*   **Isolated Workspaces**: Ensures data security by running each agent within a dedicated local file-system environment.
*   **API Gateway Orchestration**: Centralized routing via **OpenRouter** and **Ollama**, facilitating the transition from simple chatbots to goal-oriented autonomous systems.
*   **Visual Architecture**: Includes `agents_infographic.html` for an interactive look at the ecosystem.

### 🧬 Semantic Search & Embeddings
*   **Local_Embeddings.py**: High-performance text vectorization using `all-MiniLM-L6-v2` running locally.
*   **Vector Similarity Engine**: Pure **NumPy** implementation of Cosine Similarity for document comparison without external API dependencies.
*   **Efficient Processing**: Transforms text into 384-dimensional dense vectors optimized for low-latency retrieval.

### 📦 Vector Databases (RAG Readiness)
*   **chromaDB_model.py**: Implementation of a persistent local vector store using **ChromaDB**.
*   **Automated Indexing**: Handles the full lifecycle of embedding generation, storage, and metadata tagging for unstructured data.
*   **Persistent Knowledge Base**: Configured with `PersistentClient` to maintain a local data store, enabling cross-session retrieval-augmented generation (RAG) capabilities.

### 🧠 Natural Language Processing (NLP)
*   **NLP_Sentiment.py**: Emotional tone analysis powered by Hugging Face **Transformers**.
*   **Text Classification**: State-of-the-art LLM tools for categorizing text data.
*   **LangChain Integration**: Modular "Chain" workflows using **LangChain** and **Llama 3** (via Ollama) for custom prompt orchestration.

### 📈 Financial Intelligence
*   **Stock_app.py**: Streamlit dashboard featuring **LSTM** neural networks for historical price prediction.
*   **Genai_Agent.py**: Modern AI agent leveraging **Gemini 2.0 Flash** with function calling for real-time market insights via `yfinance`.
*   **Stock_Trends.py**: Technical analysis and automated trend identification.

### 🎙️ Speech & Travel Intelligence
*   **ASR_Audio_Transcriber.py**: Automated speech-to-text transcription using OpenAI’s **Whisper**.
*   **Gtts_TextToAudio.py**: Converts text to natural speech via Google Text-to-Speech (gTTS).
*   **Flight_Search_App.py**: GenAI Agent that identifies the top 3 cheapest flights with real-time pricing and direct booking links.

---

## 🛠️ Technical Stack

*   **Languages**: Python, HTML/CSS
*   **Agent Frameworks**: OpenClaw, OpenRouter, Ollama
*   **Vector DB & AI/ML**: ChromaDB, PyTorch, Sentence-Transformers, Hugging Face, LangChain, Google GenAI
*   **Data & Math**: NumPy, Pandas, Scikit-learn, YFinance
*   **Deployment**: Docker, Windows/WSL2, GitHub Actions