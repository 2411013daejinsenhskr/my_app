import streamlit as st

# 사이트 배경색을 하늘색으로 설정
st.markdown("""
    <style>
        body {
            background-color: #87CEEB;  # 하늘색
        }
    </style>
""", unsafe_allow_html=True)

# 앱 제목
st.title("이미지 링크로 이미지 띄우기")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요 (예시:https://healingfactory.co.kr/data/files/dee27b6e7d998faa5dbeb3e36762c28d.jpg)")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("확인"):
    if image_url:
        st.image(image_url, caption="입력한 이미지", use_column_width=True)
    else:
        st.write("이미지 링크를 입력해주세요.")
