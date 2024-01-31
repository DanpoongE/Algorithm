T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 행렬 리스트로 변환 완료!

    sum_flower = []
    for i in range(N):
        for j in range(M):
            flower = arr[i][j] # 시작점 꽃가루
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 이거 강사님이 알려주신 거. 상하좌우 4개밖에 없기 때문에 이렇게 하는게 편리
                ni, nj = i+di, j+dj #새로운 인덱스
                if 0<= ni < N and 0<= nj < M: # 가장자리 바깥은 생각하지 아니하겠다.
                    flower += arr[ni][nj]

            sum_flower.append(flower)

    print(f'#{tc+1} {max(sum_flower)}')
