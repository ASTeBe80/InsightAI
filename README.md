# InsightAI Documentation

## 1. Project Overview
InsightAI is a Python-based application that analyzes stock market trends and news sentiment. It uses the **Gemini AI API** for summarization and prediction, the **Alpha Vantage API** for stock market data, and **Matplotlib** for visualization. The application features a GUI built with **Tkinter** and generates **downloadable HTML reports** with insights and graphs.

## 2. Installation & Setup
### Prerequisites:
- Python 3.x
- Required libraries (install via pip):
  ```sh
  pip install requests google-generativeai matplotlib numpy pillow tkinter python-dotenv
  ```

### Setup:
1. Download or clone the project files and navigate to the project directory.
2. Create a `.env` file in the same directory as `main.py` and add your API keys:
   ```sh
   GEMINI_API_KEY=your_gemini_api_key
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## 3. How It Works
1. The user enters a **news URL** in the GUI.
2. InsightAI fetches and summarizes the news using **Gemini AI**.
3. It fetches **stock market data** from **Alpha Vantage API**.
4. The AI analyzes market trends and predicts reactions.
5. The stock data is visualized using **Matplotlib**.
6. A detailed **HTML report** is generated and saved in the Downloads folder.

## 4. Features
✔ **News Summarization**: Extracts key points from news articles.  
✔ **Stock Market Data Fetching**: Retrieves real-time stock prices.  
✔ **AI-Based Market Analysis**: Predicts market reactions.  
✔ **Graph Visualization**: Plots stock trends over 30 days.  
✔ **HTML Report Generation**: Saves insights in a styled format.  
✔ **User-Friendly GUI**: Easy interaction via Tkinter interface.

## 5. API Usage
### Google Gemini AI API
- Used for **news summarization** and **market trend analysis**.
- Requires an **API key** stored in the `.env` file.

### Alpha Vantage API
- Used for **stock market data retrieval**.
- Requires a **free API key** from [Alpha Vantage](https://www.alphavantage.co/).

## 6. Code Structure
```
InsightAI/
│── main.py  # Main GUI and application logic
│── .env  # API keys (not to be shared)
│── InsightAI logo.jpg  # Project logo
│── Documentation.md  # Project documentation
│── Presentation.pptx  # Project presentation
```

## 7. Future Improvements
- ✅ Add **user authentication** to track individual reports.
- ✅ Enable **multi-stock analysis** based on user input.
- ✅ Implement **email-based report delivery**.
- ✅ Enhance **GUI design** with better interactivity.

---
📌 **Developed by:** Ashutosh Singh  
📌 **Version:** 1.0