import streamlit as st
import requests

# Naver의 현재 날짜 가져오기
res = requests.get('https://www.naver.com/')
current_date = res.headers['Date']

# 제목과 오늘 날짜 표시
st.title('오늘 날짜')
st.write(current_date)

# 방문자 수를 파일에서 읽기
def read_visitor_count():
    try:
        with open('visitor_count.txt', 'r') as file:
            content = file.read().strip()  # 공백 제거
            if content:  # 파일 내용이 비어 있지 않으면
                count = int(content)  # 정수로 변환
            else:
                count = 0  # 비어 있을 경우 0으로 초기화
    except FileNotFoundError:
        count = 0  # 파일이 없을 경우 0으로 초기화
    except ValueError:
        count = 0  # 파일 내용이 유효하지 않을 경우 0으로 초기화
    return count

# 방문자 수를 파일에 쓰기
def write_visitor_count(count):
    with open('visitor_count.txt', 'w') as file:
        file.write(str(count))

# 방문자 수를 파일에서 읽기
visitor_count = read_visitor_count()

# 방문자 수 증가
visitor_count += 1

# 파일에 방문자 수 저장
write_visitor_count(visitor_count)

# 결과 출력
st.title("방문자 수")
st.write("현재 방문자 수:", visitor_count)

# 제목
st.title("간단한 계산기")

# 사용자 입력: 수식 입력
user_input = st.text_input("수식을 입력하세요 (예: 3 * 4)")

# 계산 버튼
if st.button("계산"):
    try:
        # eval() 함수로 수식 계산
        result = eval(user_input)
        # 결과 출력
        st.write("결과:", result)
    except Exception as e:
        st.write("오류:", str(e))









