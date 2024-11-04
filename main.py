# main.py
import streamlit as st
from page3.get_data import Lotto_class
from my_html.tab1 import display_current_numbers 
from my_html.tab2 import display_past_records    
from my_html.tab3 import draw_number    

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
tab1, tab2, tab3 = st.tabs(["현재 당첨 번호", "과거 당첨 기록", "AI 로또 추첨기"])

with tab1:
    display_current_numbers(lotto_instance)

with tab2:
    display_past_records(lotto_instance, 최근회차)

with tab3:
    # # 기존 번호 표시
    # st.write("기존 번호:")
    # draw_number(3)  # 기존에 나와 있는 3개의 번호를 출력

    # 사용자가 몇 개의 번호를 추첨할지 입력할 수 있는 텍스트 입력 필드 추가
    num_draws = st.number_input('몇 개의 추가 번호를 뽑으시겠습니까?', min_value=1, max_value=10, value=3)

    # 생성 버튼 추가
    if st.button('번호 생성'):
        st.write("생성된 번호 :")
        draw_number(num_draws)  # 입력받은 숫자를 draw_number 함수에 전달