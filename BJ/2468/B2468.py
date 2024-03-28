N = int(input())
hills = [list(map(int, input().split())) for _ in range(N)]

# 최댓값 찾기 -> 장마철 비의 양 최대치
max_height = 0
for i in range(N):      # 최대 100번 돎
    max_height = max(max(hills[i]), max_height)

for rain in range(1, max_height):
    after_rain = [[0] * N for _ in range(N)]    # 비가 내린 후 잠기는 지역 0, 안전지역 1

    for r in range(N):
        for c in range(N):
            if hills[r][c] > rain:    # 장마철 비 내리는 양보다 높이가 더 높다면
                after_rain[r][c] = 1
            # 봉우리의 높이가 더 낮다면 물에 잠김. 그대로 두면 됨

    # 자 이제 단지 찾듯이 이어진 부분 찾겠읍니다.
    safe_area = 1

