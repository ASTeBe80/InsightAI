# InsightAI Documentation

## 1. Project Overview
InsightAI is a Python-based application that analyzes stock market trends and news sentiment. It uses the **Gemini AI API** for summarization and prediction, the **Alpha Vantage API** for stock market data, and **Matplotlib** for visualization. The application features a GUI built with **Tkinter** and generates **downloadable HTML reports** with insights and graphs.

---

## **2. Installation & Setup**  

### **Prerequisites:**  
- Python 3.x  
- Required libraries (install via pip):  
  ```sh
  pip install -r requirements.txt
  ```  

### **Setup:**  
1. **Clone the repository** from GitHub:  
   ```sh
   git clone https://github.com/ASTeBe80/InsightAI.git
   cd InsightAI
   ```  
2. **Install dependencies**:  
   ```sh
   pip install -r requirements.txt
   ```  
3. **Set up API keys**:  
   - Create a `.env` file in the project root.  
   - Add your API keys:  
     ```sh
     GEMINI_API_KEY=your_gemini_api_key
     GEMINI_API_KEY2=your_gemini_api_key
     GEMINI_API_KEY3=your_gemini_api_key
     GEMINI_API_KEY4=your_gemini_api_key

     ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key

      OPENAI_API_KEY = your_openai_api_key
      OPENAI_API_KEY2 = your_openai_api_key
      OPENAI_API_KEY3 = your_openai_api_key
     ```  
4. **Run the application**:  
   ```sh
   python openaimain.py
   ```

---

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

## 6. Future Improvements
- ✅ Add **user authentication** to track individual reports.
- ✅ Enable **multi-stock analysis** based on user input.
- ✅ Implement **email-based report delivery**.
- ✅ Enhance **GUI design** with better interactivity.

---
📌 **Developed by:** Ashutosh Singh  
📌 **Version:** 1.0
📌 **License:** MIT