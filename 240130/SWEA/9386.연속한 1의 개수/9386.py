T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    serial = []
    cnt = 0

    for i in range(N):
        if arr[i] == 0:             # 값이 0일 때
            if cnt != 0:            # cnt가 쌓인게 있으면
                serial.append(cnt)  # 그거 serial 리스트에 넣어주고
            cnt = 0                 # cnt를 초기화합니다

        else:                       # 값이 1이라면
            cnt += 1                # 우선 cnt1을 더해주고
            if i == N-1:              # 만일 끝 인덱스다!
                serial.append(cnt)  # 지금까지 쌓인 cnt를 serial에 더해줍니다.
    print(f'#{tc} {max(serial)}')
