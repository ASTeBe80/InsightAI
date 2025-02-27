import os
import requests
import openai
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from PIL import Image, ImageTk

# Load API keys
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY3")
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

# Check if the API key is loaded
if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please check your .env file.")

openai.api_key = openai_api_key

# Logo Path
logo_path = "C:\\Users\\HP\\OneDrive\\Desktop\\InsightAI v1.0\\InsightAI logo.jpg"

def fetch_news_summary(news_url):
    sys_prompt = f"""
        Summarize the news article from the following URL in 4-5 lines.
        URL: {news_url}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can change this to another model if needed
            messages=[{"role": "user", "content": sys_prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error fetching news summary: {e}"

def fetch_stock_data():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey={alpha_vantage_api_key}"
    response = requests.get(url)
    data = response.json()
    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    return None

def analyze_market_reaction(stock_data, news_url):
    sys_prompt = f"""
        Analyze the following stock market data and predict how the market will react based on recent trends in News.
        Ensure that the output is short and listed in order.
        Data: {stock_data}
        News: {news_url}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can change this to another model if needed
            messages=[{"role": "user", "content": sys_prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error analyzing market reaction: {e}"

def plot_stock_graph(stock_data):
    dates = list(stock_data.keys())[:30][::-1]
    prices = [float(stock_data[date]["4. close"]) for date in dates]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='purple', label='Stock Prices')
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.title("Stock Market Trend Over the Last 30 Days")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    graph_path = os.path.join(downloads_folder, "stock_graph.png")
    plt.savefig(graph_path)
    plt.close()  # Close the plot to free up memory
    return graph_path

def get_unique_filename(base_path):
    if not os.path.exists(base_path):
        return base_path
    counter = 1
    while os.path.exists(f"{base_path[:-5]}({counter}).html"):
        counter += 1
    return f"{base_path[:-5]}({counter}).html"

def generate_html_report(news_summary, market_analysis, graph_path):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(downloads_folder, "stock_analysis_report.html")
    unique_output_file = get_unique_filename(output_file)
    
    html_content = f"""
    <html>
    <head>
        <title>Stock Market Analysis Report</title>
        <style>
            body {{ background-color: #121212; color: #ffffff; font-family: Arial, sans-serif; }}
            .container {{ width: 80%; margin: auto; }}
            h1, h2 {{ color: #bb86fc; }}
            img {{ width: 100%; border-radius: 10px; }}
            .graph-description {{ margin-top: 10px; font-size: 14px; }}
            .summary {{ margin-top: 20px; padding: 10px; background-color: #1e1e1e; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="file://{logo_path}" alt="InsightAI Logo" style="width: 200px; display: block; margin: auto;">
            <h1>Stock Market Analysis Report</h1>
            <h2>News Summary</h2>
            <p class="summary">{news_summary}</p>
            <h2>Stock Market Prediction</h2>
            <img src="file://{graph_path}" alt="Stock Market Graph">
            <p class="graph-description">The graph above represents the last 30 days of stock prices for SPY, a popular ETF tracking the S&P 500. Based on trends, the AI has predicted how the market might react.</p>
            <h2>Market Analysis</h2>
            <p class="summary">{market_analysis}</p>
        </div>
    </body>
    </html>
    """
    
    with open(unique_output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    messagebox.showinfo("Success", f"Report saved in: {unique_output_file}")

def run_analysis():
    news_url = url_entry.get()
    if not news_url:
        messagebox.showerror("Error", "Please enter a news URL")
        return
    
    news_summary = fetch_news_summary(news_url)
    stock_data = fetch_stock_data()
    if stock_data:
        market_analysis = analyze_market_reaction(stock_data, news_url)
        graph_path = plot_stock_graph(stock_data)
        generate_html_report(news_summary, market_analysis, graph_path)
    else:
        messagebox.showerror("Error", "Error fetching stock data.")

# GUI Setup
root = tk.Tk()
root.title("InsightAI - Stock Market Analysis")
root.geometry("500x400")
root.configure(bg="#121212")

# Add Logo to GUI
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((200, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="#121212")
logo_label.pack(pady=10)

tk.Label(root, text="Enter News Article URL:", bg="#121212", fg="#bb86fc").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Generate Report", command=run_analysis, bg="#bb86fc", fg="white").pack(pady=20)

root.mainloop()