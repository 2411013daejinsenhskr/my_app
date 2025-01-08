import streamlit as st

# 앱 제목
st.title("이미지 링크로 이미지 띄우기")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요 (예시:https://healingfactory.co.kr/data/files/dee27b6e7d998faa5dbeb3e36762c28d.jpg)")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("확인"):
    if image_url:
        # 이미지 출력과 함께 레인보우 테두리 애니메이션을 적용
        st.markdown(f"""
        <style>
            .rainbow-border {{
                border: 10px solid;
                border-radius: 10px;
                animation: rainbow-border 5s infinite;
                display: inline-block;
                padding: 10px;
            }}
            @keyframes rainbow-border {{
                0% {{ border-color: red; }}
                14% {{ border-color: orange; }}
                28% {{ border-color: yellow; }}
                42% {{ border-color: green; }}
                57% {{ border-color: blue; }}
                71% {{ border-color: indigo; }}
                85% {{ border-color: violet; }}
                100% {{ border-color: red; }}
            }}
        </style>
        <div class="rainbow-border">
            <img src="{image_url}" alt="입력한 이미지" width="100%" />
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("이미지 링크를 입력해주세요.")
