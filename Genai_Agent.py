from google import genai
from google.genai import types
import yfinance as yf
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st

# Load credentials
load_dotenv(find_dotenv())
API_KEY = os.getenv("GEMINI_API_KEY")

# --- STEP 1: DEFINE TOOLS FIRST (Fixes NameError) ---
def get_stock_price(ticker: str) -> str:
    """Fetches the current real-time stock price for a company."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.fast_info['last_price']
        return f"The current price of {ticker} is ${price:.2f}"
    except Exception as e:
        return f"Error fetching price: {str(e)}"

# Define the tools list here so it is available to the client
tools_list = [get_stock_price]

# --- STEP 2: INITIALIZE THE MODERN CLIENT ---
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-2.0-flash"

# --- STEP 3: STREAMLIT UI ---
st.title("📈 AI Market Agent")
ticker_input = st.text_input("Enter Ticker", "AAPL")

if st.button("Run Agent Analysis"):
    if not API_KEY:
        st.error("API Key missing! Check your .env file.")
    else:
        try:
            # Automatic function calling lets the agent use your get_stock_price tool
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=f"Give me a market update for {ticker_input}. Use your tool to find the price.",
                config=types.GenerateContentConfig(
                    tools=tools_list,
                    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
                )
            )
            
            st.markdown("### Agent Analysis")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Agent Error: {e}")
#python -m streamlit run "C:\Users\ADMIN\My Drive\Python\AI_agents\Genai_Agent.py"