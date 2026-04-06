import yfinance as yf
import ollama  # pip install ollama

def get_stock_news_and_impact(ticker):
    # 1. Fetch news from Yahoo Finance
    print(f"--- Fetching news for {ticker} ---")
    stock = yf.Ticker(ticker)
    news_list = stock.news[:5]
    
    if not news_list:
        return "No recent news found."

    headlines = ""
    for item in news_list:
        title = item.get('title') or item.get('headline') or "No Title"
        headlines += f"- {title}\n"

    # 2. Call your local DeepSeek-R1 model
    print(f"--- Local DeepSeek-R1 is thinking... ---")
    
    prompt = f"""
    Analyze these headlines for {ticker} and explain the price impact. 
    Provide a sentiment and a confidence score.
    
    Headlines:
    {headlines}
    """

    # This talks to the 'ollama run deepseek-r1:7b' you just started
    response = ollama.chat(
        model='deepseek-r1:7b',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']

if __name__ == "__main__":
    ticker_symbol = input("Enter ticker: ").strip().upper()
    print(get_stock_news_and_impact(ticker_symbol))