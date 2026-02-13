import yfinance as yf
import ollama  # pip install ollama

def get_stock_news_and_impact(ticker):
    try:
        print(f"--- Fetching news for {ticker} ---")
        stock = yf.Ticker(ticker)
        news_list = stock.news[:5]
        
        if not news_list:
            return "No recent news found."

        headlines = ""
        for item in news_list:
            title = item.get('title') or item.get('headline') or "No Title"
            headlines += f"- {title}\n"

        # 3. Using DeepSeek-R1 locally for FREE
        print(f"--- DeepSeek-R1 is thinking... ---")
        
        prompt = f"Analyze these headlines for {ticker} and explain the price impact: \n{headlines}"

        response = ollama.chat(
            model='deepseek-r1:7b',
            messages=[{'role': 'user', 'content': prompt}]
        )

        return response['message']['content']
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    ticker_symbol = input("Enter ticker: ").strip().upper()
    print(get_stock_news_and_impact(ticker_symbol))