import streamlit as st

# 앱 제목
st.title("이미지 링크로 이미지 띄우기")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요 (예시:https://healingfactory.co.kr/data/files/dee27b6e7d998faa5dbeb3e36762c28d.jpg)")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("확인"):
    if image_url:
        # 이미지 출력
        st.image(image_url, caption="입력한 이미지", use_column_width=True)
        
        # HTML과 JavaScript를 사용하여 비처럼 내리는 이미지 효과 구현
        st.markdown(f"""
        <style>
        body {{
            background-color: #f0f0f0;
            position: relative;
            height: 100vh;
            overflow: hidden;
        }}
        .falling-image {{
            position: absolute;
            animation: fall 5s infinite;
            opacity: 0.8;
        }}
        @keyframes fall {{
            0% {{
                top: -100px;
                left: {random.randint(0, 100)}%;
                transform: rotate(0deg);
            }}
            100% {{
                top: 100vh;
                left: {random.randint(0, 100)}%;
                transform: rotate(360deg);
            }}
        }}
        </style>
        <script>
        let imageCount = 20;  // 이미지 갯수 조정
        for (let i = 0; i < imageCount; i++) {{
            let img = document.createElement('img');
            img.src = '{image_url}';
            img.classList.add('falling-image');
            img.style.width = '50px'; // 이미지 크기 조정
            img.style.animationDelay = Math.random() * 5 + 's';  // 애니메이션 지연 시간 랜덤
            document.body.appendChild(img);
        }}
        </script>
        """, unsafe_allow_html=True)
        
    else:
        st.write("이미지 링크를 입력해주세요.")
