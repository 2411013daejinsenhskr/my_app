import streamlit as st
import random

# 앱 제목
st.title("움직이는 이미지 띄우기")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요 (예시:https://healingfactory.co.kr/data/files/dee27b6e7d998faa5dbeb3e36762c28d.jpg)")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("확인"):
    if image_url:
        # HTML, CSS, JavaScript로 이미지가 움직이도록 설정
        st.components.v1.html(f"""
        <style>
            .moving-image {{
                position: absolute;
                width: 100px;  /* 이미지 크기 */
                height: auto;
                border-radius: 10px;
                border: 5px solid #FF5733;  /* 테두리 설정 */
            }}
        </style>

        <div class="moving-image">
            <img src="{image_url}" alt="입력한 이미지" width="100%" />
        </div>

        <script>
            var img = document.querySelector('.moving-image img');
            var container = document.body;
            var directionX = 1;
            var directionY = 1;
            var speed = 3;
            var posX = 0;
            var posY = 0;

            function moveImage() {{
                posX += speed * directionX;
                posY += speed * directionY;

                // 벽에 닿으면 방향을 반대로 바꿈
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
        """, height=600, width=800)
    else:
        st.write("이미지 링크를 입력해주세요.")
