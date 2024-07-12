import streamlit as st
import yfinance as yf

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app.')
ticker = st.text_input('Enter Stock Ticker', 'AAPL')
