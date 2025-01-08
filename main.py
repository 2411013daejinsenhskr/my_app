import streamlit as st
import random
import time

# 게임 초기화
def game_reset():
    return {
        "ball_pos": [300, 400],
        "ball_velocity": [random.choice([-5, 5]), -5],
        "paddle_pos": 250,
        "bricks": [list(range(i * 100, i * 100 + 80)) for i in range(5)],
        "score": 0
    }

# 게임 로직
def update_game_state(game_state):
    # 공의 위치 업데이트
    game_state["ball_pos"][0] += game_state["ball_velocity"][0]
    game_state["ball_pos"][1] += game_state["ball_velocity"][1]
    
    # 벽 충돌 체크
    if game_state["ball_pos"][0] <= 0 or game_state["ball_pos"][0] >= 600:
        game_state["ball_velocity"][0] = -game_state["ball_velocity"][0]
    if game_state["ball_pos"][1] <= 0:
        game_state["ball_velocity"][1] = -game_state["ball_velocity"][1]
    
    # 패들 충돌 체크
    if (game_state["ball_pos"][1] >= 460 and
        game_state["ball_pos"][0] >= game_state["paddle_pos"] and
        game_state["ball_pos"][0] <= game_state["paddle_pos"] + 80):
        game_state["ball_velocity"][1] = -game_state["ball_velocity"][1]
    
    # 벽돌 충돌 체크
    for brick in game_state["bricks"]:
        if (game_state["ball_pos"][1] >= 50 and
            game_state["ball_pos"][0] >= brick[0] and
            game_state["ball_pos"][0] <= brick[0] + 80):
            game_state["bricks"].remove(brick)
            game_state["ball_velocity"][1] = -game_state["ball_velocity"][1]
            game_state["score"] += 10
            break
    
    return game_state

# 게임 화면 출력
def draw_game(game_state):
    st.write(f"Score: {game_state['score']}")
    st.write(f"Ball Position: {game_state['ball_pos']}")
    st.write(f"Paddle Position: {game_state['paddle_pos']}")
    st.write("Bricks Remaining: ", len(game_state['bricks']))

# 메인 게임
def main():
    st.title("벽돌깨기 게임")

    game_state = game_reset()
    
    # 패들 이동
    move_left = st.button("왼쪽으로 이동")
    move_right = st.button("오른쪽으로 이동")
    
    if move_left:
        game_state["paddle_pos"] = max(game_state["paddle_pos"] - 10, 0)
    if move_right:
        game_state["paddle_pos"] = min(game_state["paddle_pos"] + 10, 520)
    
    # 게임 업데이트
    game_state = update_game_state(game_state)
    
    # 게임 화면 그리기
    draw_game(game_state)
    
    # 게임이 끝났을 때
    if not game_state["bricks"]:
        st.write("게임 종료! 점수: ", game_state["score"])
        if st.button("게임 다시 시작"):
            game_state = game_reset()

    time.sleep(0.02)  # 게임 속도 조절

if __name__ == "__main__":
    main()
