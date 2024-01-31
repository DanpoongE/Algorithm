T = int(input())

for t in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 행에서 연속된 1의 갯수 찾기
    for i in range(N):
        counts = 0
        for j in range(N):
            if arr[i][j] == 1:
                counts += 1
            else: # 1이 아닌 수가 나오면 그 전까지 3이었을 경우 result값 1개 오르고, counts 재카운트
                if counts == 3:
                    result +=1
                counts = 0
        if counts == K:
            result += 1

    # 열에서 연속된 1의 갯수 찾기
    for j in range(N):
        counts = 0
        for i in range(N):
            if arr[i][j] == 1:
                counts += 1
            else:
                if counts == 3:
                    result +=1
                counts = 0
        if counts == K:
            result += 1

    print(result)