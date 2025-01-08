import streamlit as st

# 앱 제목
st.title("이미지 링크로 벽돌깨기 게임")

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input("이미지 링크를 입력하세요 (예시: https://healingfactory.co.kr/data/files/dee27b6e7d998faa5dbeb3e36762c28d.jpg)")

# "확인" 버튼 클릭 시 이미지 출력
if st.button("게임 시작"):
    if image_url:
        # HTML, CSS, JavaScript로 벽돌깨기 게임 구현
        st.markdown(f"""
        <style>
            body {{
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
                overflow: hidden;
            }}
            .brick {{
                position: absolute;
                width: 100px;
                height: 30px;
                background-image: url("{image_url}");
                background-size: cover;
                border-radius: 5px;
                animation: rainbow-border 1s infinite;
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
        
        <div id="game-container" style="position: relative; width: 100%; height: 400px; overflow: hidden; background-color: #c1e0e7;">
            <!-- 벽돌을 화면에 배치할 공간 -->
        </div>

        <script>
            var gameContainer = document.getElementById('game-container');
            var bricks = [];
            var brickWidth = 100;  // 벽돌 가로 크기
            var brickHeight = 30;  // 벽돌 세로 크기

            // 벽돌을 5개 생성해서 게임 화면에 배치
            for (var i = 0; i < 5; i++) {{
                var brick = document.createElement('div');
                brick.classList.add('brick');
                brick.style.top = (50 + (i * (brickHeight + 10))) + 'px';  // 벽돌 세로 위치
                brick.style.left = (100 + (i * (brickWidth + 10))) + 'px';  // 벽돌 가로 위치
                gameContainer.appendChild(brick);
                bricks.push(brick);
            }}

            // 게임 요소를 벽돌로 바꿔주고 애니메이션을 적용
            var ball = document.createElement('div');
            ball.style.position = 'absolute';
            ball.style.width = '20px';
            ball.style.height = '20px';
            ball.style.backgroundColor = 'red';
            ball.style.borderRadius = '50%';
            ball.style.left = '200px';
            ball.style.top = '350px';
            gameContainer.appendChild(ball);

            var directionX = 2;
            var directionY = -2;
            var ballSpeed = 4;

            function moveBall() {{
                var ballRect = ball.getBoundingClientRect();
                var containerRect = gameContainer.getBoundingClientRect();

                // 벽과 충돌 처리
                if (ballRect.left <= containerRect.left || ballRect.right >= containerRect.right) {{
                    directionX *= -1;  // 벽에 튕기면 방향 변경
                }}
                if (ballRect.top <= containerRect.top) {{
                    directionY *= -1;  // 상단 벽에 튕기면 방향 변경
                }}

                // 바닥에 닿으면 게임 오버
                if (ballRect.bottom >= containerRect.bottom) {{
                    alert("게임 오버!");
                    location.reload();  // 게임 리셋
                }}

                ball.style.left = (ball.offsetLeft + directionX) + 'px';
                ball.style.top = (ball.offsetTop + directionY) + 'px';

                // 벽돌과 충돌 체크
                bricks.forEach(function(brick, index) {{
                    var brickRect = brick.getBoundingClientRect();
                    if (ballRect.left < brickRect.right && ballRect.right > brickRect.left && 
                        ballRect.top < brickRect.bottom && ballRect.bottom > brickRect.top) {{
                        // 벽돌 충돌 처리
                        directionY *= -1;
                        brick.style.display = 'none';  // 벽돌 숨기기
                        bricks.splice(index, 1);  // 벽돌 리스트에서 제거
                    }}
                }});

                requestAnimationFrame(moveBall);  // 애니메이션 프레임 계속 호출
            }}
            moveBall();  // 공 움직이기 시작
        </script>
        """, unsafe_allow_html=True)
    else:
        st.write("이미지 링크를 입력해주세요.")
