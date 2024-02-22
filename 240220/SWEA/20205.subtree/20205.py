T = int(input())

for tc in range(1, T+1):
    E, N = list(map(int, input().split()))

    node_info = [[] for _ in range(E+2)]

    arr = list(map(int, input().split()))

    for i in range(0, E*2, 2):
        node_info[arr[i]].append(arr[i+1])

    # print(node_info)

    stack = []
    stack.append(N)
    result = 1

    while stack:        # 자식이 있을 때까지
        p = stack.pop()

        for i in node_info[p]:      # 자식 노드 확인
            stack.append(i)
            result += 1

    print(f'#{tc} {result}')
