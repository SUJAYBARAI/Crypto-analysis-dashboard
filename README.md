# Cryptocurrency Trend Analysis Dashboard

## 📌 Project Overview

This is an interactive cryptocurrency analysis dashboard built using **Streamlit**. It allows users to analyze the historical performance of popular cryptocurrencies like **Bitcoin (BTC)**, **Ethereum (ETH)**, and **Solana (SOL)** using data from **Yahoo Finance (yFinance)**.

### 🔍 Features
- View **price trends**, **daily returns**, **volatility**, and **RSI (Relative Strength Index)**.
- Select different cryptocurrencies from a dropdown menu.
- Set **custom date range** to filter data.
- Beautiful, interactive visualizations using **Matplotlib** and **Seaborn**.

---

## ⚙️ Installation

Make sure Python is installed (version 3.8+ recommended).

### Step-by-step:

```bash
# 1. Clone the repository
git clone https://github.com/SUJAYBARAI/Crypto-analysis-dashboard.git

# 2. Navigate into the project folder
cd crypto-analysis-dashboard

# 3. (Optional) Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 4. Install the dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

---

## 💻 How to Use

- Select a **cryptocurrency** (BTC, ETH, SOL) from the sidebar.
- Pick a **start and end date** using the date picker.
- Dashboard automatically updates with:
  - Price chart 📈
  - Daily returns histogram 📊
  - Volatility and RSI plots 📉

---

## 🖼️ Screenshot

![Dashboard Preview](https://github.com/SUJAYBARAI/Crypto-analysis-dashboard/blob/main/Screenshot.png)

---

## 🤝 Contributing

Want to improve this project?

1. Fork the repo  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a pull request ✅

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use it for learning or your portfolio.

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Yahoo Finance API (yfinance)](https://pypi.org/project/yfinance/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
