T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    end_point = arr[N - 1][N - 1]
    start_r = 0
    start_c = 0
    start_point = arr[start_r][start_c]
    result += start_point       # 먼저 시작점 값 result에 합산

    # 일단 최단거리로 풀어보자. 우측과 아래만 비교하는 방식으로.
    while start_r != N - 1 and start_c != N - 1:

        # 이제 양 옆 비교. 행렬 범위 내에서 탐색
        if start_r + 1 < N and start_c + 1 < N:
            if arr[start_r + 1][start_c] >= arr[start_r][start_c + 1]:   # 아래보다 오른쪽이 더 작은값이라면
                start_c = start_c + 1   # 오른쪽으로 한 칸 이동하고
                result += arr[start_r][start_c] # 해당 값 합산

            elif arr[start_r][start_c + 1] > arr[start_r + 1][start_c]: # 아래가 더 작은 값이면
                start_r = start_r + 1
                result += arr[start_r][start_c]

            if start_r == N - 1:        # 행이 끝에 다다랐으면 이제 오른쪽으로만 가야지
                result += arr[start_r][start_c + 1]
                start_c = start_c + 1

            if start_c == N - 1:        # 열이 끝에 다다랐으면 이제 밑으로만 가야지
                result +=  arr[start_r + 1][start_c]
                start_r = start_r + 1

    print(f'#{tc}', result)