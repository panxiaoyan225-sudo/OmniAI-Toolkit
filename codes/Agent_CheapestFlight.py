import os
import requests
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv, find_dotenv

# --- 1. SET UP THE WEB PAGE ---
st.set_page_config(page_title="OmniAI Flight Finder", page_icon="✈️")
st.title("✈️ OmniAI Flight Finder")

# --- 2. CONFIGURATION ---
load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY")

# --- 3. THE UPDATED TOOL ---
def get_top_cheapest_flights(origin: str, destination: str, date: str) -> str:
    """Fetches the top 3 cheapest flights with direct booking links."""
    if not FLIGHT_API_KEY:
        return "Error: FLIGHT_API_KEY is missing."

    url = f"https://api.flightapi.io/onewaytrip/{FLIGHT_API_KEY}/{origin}/{destination}/{date}/1/0/0/Economy/USD"
    
    try:
        response = requests.get(url)
        data = response.json()
        itineraries = data.get('itineraries', [])
        
        if not itineraries:
            return f"No flights found from {origin} to {destination} on {date}."

        # Sort all flights by price
        sorted_flights = sorted(itineraries, key=lambda x: x['pricing_options'][0]['price']['amount'])
        
        results = [f"### 🎫 Top 3 Deals for {origin} → {destination}"]
        for i, flight in enumerate(sorted_flights[:3], 1):
            price_data = flight['pricing_options'][0]
            price = price_data['price']['amount']
            agent = price_data.get('agent_ids', ['Agent'])[0]
            # Use the 'url' field for direct booking
            booking_url = price_data.get('url', 'https://www.google.com/flights')
            
            results.append(
                f"**{i}. ${price:.2f} via {agent.title()}**\n"
                f"👉 [Click to Book this Flight]({booking_url})"
            )
            
        return "\n\n".join(results)
    except Exception as e:
        return f"System Error: {str(e)}"

# --- 4. INITIALIZATION ---
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
    tools_list = [get_top_cheapest_flights]
else:
    st.error("Missing GEMINI_API_KEY.")

# --- 5. WEBSITE UI ---
col1, col2, col3 = st.columns(3)
with col1: origin_city = st.text_input("Origin (IATA)", value="YOW")
with col2: dest_city = st.text_input("Destination (IATA)", value="YYZ")
with col3: travel_date = st.date_input("Travel Date")

if st.button("Search Best Deals"):
    formatted_date = travel_date.strftime("%Y-%m-%d")
    prompt = f"Find me the 3 cheapest flights from {origin_city} to {dest_city} on {formatted_date}."
    
    with st.spinner("Finding live booking links..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=tools_list,
                    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
                )
            )
            st.markdown("---")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Agent Error: {e}")