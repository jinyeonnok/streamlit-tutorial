# main.py
import streamlit as st

import requests


res = requests.get('https://www.naver.com/')
print(res.headers['Date'])

st.title(str(res.headers['Date']))

