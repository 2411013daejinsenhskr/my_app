import streamlit as st

# 앱 제목
st.title("이미지 링크로 이미지 띄우기")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요:")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("확인"):
    if image_url:
        st.image(image_url, caption="입력한 이미지", use_column_width=True)
    else:
        st.write("이미지 링크를 입력해주세요.")
