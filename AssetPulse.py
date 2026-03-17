import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="AssetPulse", 
    page_icon="📈", 
    layout="wide"
)

st.title("📈 AssetPulse: Mini Tracker")
st.markdown("Enter a stock or crypto ticker to see its performance over time.")

st.sidebar.header("User Input")

ticker_input = st.sidebar.text_input(
    "Ticker Symbol", 
    value="BTC-USD", 
    help="e.g., AAPL, TSLA, BTC-USD, ETH-USD"
).upper()

days = st.sidebar.slider("Days of History", min_value=7, max_value=365, value=30)

run_button = st.sidebar.button("Update Data")

@st.cache_data
def load_data(symbol, period_days):
    try:
        
        data = yf.download(symbol, period=f"{period_days}d", interval="1d")
        
        if data.empty:
            return None
        
        
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        return data['Close']
    except Exception:
        return None

if ticker_input:
    with st.spinner(f"Fetching data for {ticker_input}..."):
        chart_data = load_data(ticker_input, days)

    if chart_data is not None:
        
        current_price = float(chart_data.iloc[-1])
        start_price = float(chart_data.iloc[0])
        price_diff = current_price - start_price
        percent_change = (price_diff / start_price) * 100

        
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"${current_price:,.2f}")
        col2.metric("Price Change", f"${price_diff:,.2f}", delta=f"{price_diff:,.2f}")
        col3.metric("Percent Change", f"{percent_change:.2f}%", delta=f"{percent_change:.2f}%")

        st.subheader(f"{ticker_input} Price Trend (Last {days} Days)")
        st.line_chart(chart_data)

        if st.checkbox("Show Raw Data"):
            st.dataframe(chart_data)
    else:
        st.error(f"Could not find data for '{ticker_input}'. Please check the symbol and try again.")
else:
    st.info("Please enter a ticker symbol in the sidebar to begin.")

st.divider()
st.caption("Powered by Streamlit and YFinance API")