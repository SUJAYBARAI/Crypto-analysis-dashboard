import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Configure page
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

# Title
st.title("📊 Cryptocurrency Trend Analysis Dashboard")
st.markdown("Analyze the trends, returns, and volatility of your selected cryptocurrency.")

# Sidebar Inputs
st.sidebar.header("User Input")

# Safe date range setup (starting from 2014)
min_date = datetime.date(2014, 1, 1)  # Bitcoin's earliest available data
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# Dropdown for crypto
crypto = st.sidebar.selectbox(
    "Select Cryptocurrency",
    options=['Select', 'BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD', 'DOGE-USD']
)

# Date input with safe max range
start_date = st.sidebar.date_input("Start Date", min_value=min_date, max_value=yesterday, value=min_date)
end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=yesterday, value=yesterday)

# Date check
if start_date > end_date:
    st.error("❌ Start date cannot be after end date.")

# Proceed only if valid input is selected
elif crypto != 'Select' and start_date and end_date:
    try:
        # Ensure end_date is not today (avoid empty DataFrame on Streamlit Cloud)
        if end_date >= datetime.date.today():
            end_date = datetime.date.today() - datetime.timedelta(days=1)

        # Fetch data
        df = yf.download(
            crypto,
            start=start_date,
            end=end_date,
            progress=False,
            threads=False
        )
        df.dropna(inplace=True)

        if df.empty:
            st.warning("⚠️ No data found. Try a different crypto or date range.")
            st.write("Debug info:", crypto, start_date, end_date)  # optional debug
        else:
            st.success(f"✅ Data loaded for {crypto} from {start_date} to {end_date}")

            # Show raw data
            st.subheader("🔹 Latest Price Data")
            st.dataframe(df.tail())

            # Price Trend
            st.subheader("📈 Price Trend")
            st.line_chart(df['Close'])

            # Daily Returns
            df['Daily Return %'] = df['Close'].pct_change() * 100
            st.subheader("📉 Daily Return (%)")
            st.line_chart(df['Daily Return %'])

            # Moving Averages
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df['SMA_50'] = df['Close'].rolling(window=50).mean()

            st.subheader("📊 Moving Averages (20 & 50 Days)")
            fig, ax = plt.subplots()
            ax.plot(df['Close'], label='Close Price', linewidth=2)
            ax.plot(df['SMA_20'], label='SMA 20', linestyle='--')
            ax.plot(df['SMA_50'], label='SMA 50', linestyle='--')
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")
            ax.legend()
            st.pyplot(fig)

            # Volatility
            df['Volatility'] = df['Daily Return %'].rolling(window=20).std()
            st.subheader("⚡ Volatility (20-day STD)")
            st.line_chart(df['Volatility'])

            # Cumulative Return
            df['Cumulative Return'] = (df['Close'] / df['Close'].iloc[0] - 1) * 100
            st.subheader("📊 Cumulative Return")
            st.line_chart(df['Cumulative Return'])

            # RSI (14-day)
            delta = df['Close'].diff()
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)

            avg_gain = gain.rolling(window=14).mean()
            avg_loss = loss.rolling(window=14).mean()

            rs = avg_gain / avg_loss
            df['RSI'] = 100 - (100 / (1 + rs))

            st.subheader("📉 RSI (14-day)")
            st.line_chart(df['RSI'])

    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")

else:
    st.info("ℹ️ Please select a cryptocurrency and a valid date range to begin.")
