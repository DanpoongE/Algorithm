T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)

    result = 0
    for i in range(N):          # 이제 한줄씩 갑니다
        if arr[i] > 0:          # 빌딩 높이가 0보다 크면
            bld_val = []        # 높이 비교할 리스트 만들고
            for di in [-2, -1, 1, 2]:    # 좌우 2개 빌딩 높이를
                bld_val.append(arr[i+di])   # 리스트에 넣을게요
            # print(bld_val)
            # print(max(bld_val))
            view = arr[i] - max(bld_val)    # 조망권확보수 = 현재건물높이 - max
            if view >= 0:
                # print(view)
                result += view
    print(f'#{tc} {result}')