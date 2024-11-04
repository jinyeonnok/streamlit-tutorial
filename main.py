# main.py
import streamlit as st
from page3.get_data import Lotto_class
from my_html import tab1, tab2

# Lotto_class의 인스턴스 생성
lotto_instance = Lotto_class()

st.title('이번주 당첨번호')

최근회차 = lotto_instance.최근회차()
st.title(f'최근 회차 : {최근회차}')

# HTML 및 CSS 스타일
st.markdown("""
<style>
    .lotto-ball {
        display: inline-block;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        color: white;
        text-align: center;
        line-height: 50px;
        font-size: 20px;
        margin: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
    .lotto-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 탭 추가
tab1, tab2 = st.tabs(["현재 당첨 번호", "과거 당첨 기록"])

with tab1:
    tab1.display_current_numbers(lotto_instance)

# with tab2:
#     tab2.display_past_records(lotto_instance, 최근회차)

