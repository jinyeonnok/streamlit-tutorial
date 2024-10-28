# main.py
import streamlit as st

import requests


res = requests.get('https://www.naver.com/')
print(res.headers['Date'])

st.title('오늘날짜',str(res.headers['Date']))

import streamlit as st

# 제목
st.title("간단한 계산기")

# 사용자 입력
num1 = st.number_input("첫 번째 숫자", value=0.0)
num2 = st.number_input("두 번째 숫자", value=0.0)

# 연산자 선택
operation = st.selectbox("연산 선택", ["덧셈", "뺄셈", "곱셈", "나눗셈"])

# 계산 버튼
if st.button("계산"):
    if operation == "덧셈":
        result = num1 + num2
    elif operation == "뺄셈":
        result = num1 - num2
    elif operation == "곱셈":
        result = num1 * num2
    elif operation == "나눗셈":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "오류: 0으로 나눌 수 없습니다."

    # 결과 출력
    st.write("결과:", result)
