def combi(idx):
    if idx == M:  # 부분집합의 개수가 M과 같으면 return
        print(*arr)
        return

    for num in range(1, N+1):
        if not used[num]:
            arr[idx] = str(num)
            used[num] = True
            combi(idx+1)
            used[num] = False

N, M = map(int, input().split())
arr = [''] * M  # 부분집합 배열
used = [False] * (N+1)  # 숫자 사용 여부 배열

combi(0)



