import streamlit as st
import requests

# Naver의 현재 날짜 가져오기
res = requests.get('https://www.naver.com/')
print(res.headers['Date'])

st.title('오늘 날짜')
st.write(res.headers['Date'])

# 제목
st.title("간단한 계산기")

# 사용자 입력: 수식 입력
user_input = st.text_input("수식을 입력하세요 (예: 3 * 4)", "")

# 계산 버튼
calculate = st.button("계산")

# 엔터가 눌렸을 때 계산 버튼 클릭한 것처럼 처리
if user_input and (calculate or st.session_state.get('last_input') != user_input):
    try:
        # eval() 함수로 수식 계산
        result = eval(user_input)
        # 결과 출력
        st.write("결과:", result)
        # 마지막 입력값 저장
        st.session_state['last_input'] = user_input
    except Exception as e:
        st.write("오류:", str(e))
