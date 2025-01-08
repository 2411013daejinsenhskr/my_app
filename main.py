import streamlit as st

# 앱 제목
st.title("움직이는 이미지 띄우기")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요 (예시:https://healingfactory.co.kr/data/files/dee27b6e7d998faa5dbeb3e36762c28d.jpg)")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("확인"):
    if image_url:
        # HTML, CSS, JavaScript를 사용해 이미지가 움직이도록 설정
        st.markdown(f"""
        <style>
        @keyframes move {
            0% {{
                left: 0%;
                top: 50%;
            }}
            25% {{
                left: 90%;
                top: 10%;
            }}
            50% {{
                left: 0%;
                top: 90%;
            }}
            75% {{
                left: 90%;
                top: 50%;
            }}
            100% {{
                left: 0%;
                top: 50%;
            }}
        }}
        
        .moving-image {{
            position: absolute;
            animation: move 5s infinite ease-in-out;
            width: 100px; /* 이미지 크기 */
            border-radius: 10px;
            border: 5px solid #FF5733; /* 테두리 설정 */
        }}
        </style>

        <div class="moving-image">
            <img src="{image_url}" alt="입력한 이미지" width="100%" />
        </div>

        <script>
            var img = document.querySelector('.moving-image');
            var container = document.body;
            var directionX = 1;
            var directionY = 1;
            var speed = 5;
            var posX = 0;
            var posY = 0;

            function moveImage() {{
                posX += speed * directionX;
                posY += speed * directionY;
                
                if (posX >= container.clientWidth - img.offsetWidth || posX <= 0) {{
                    directionX *= -1;
                }}
                if (posY >= container.clientHeight - img.offsetHeight || posY <= 0) {{
                    directionY *= -1;
                }}
                
                img.style.left = posX + 'px';
                img.style.top = posY + 'px';

                requestAnimationFrame(moveImage);
            }}
            moveImage();
        </script>
        """, unsafe_allow_html=True)
    else:
        st.write("이미지 링크를 입력해주세요.")
