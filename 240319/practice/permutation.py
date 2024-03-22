arr = [i for i in range(1, 4)]
path = [0] * len(arr)

def permutation(level):
    if level == 3:
        print(*path)
        return

    for i in range(len(arr)):
        if arr[i] in path:  # 이미 쓴 수면
            continue

        path[level] = arr[i]
        dfs(level + 1)

        # 갔다 와서 할 로직
        # 기존 방문 초기화
        path[level] = 0