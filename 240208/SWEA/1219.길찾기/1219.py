for _ in range(10):
    tc, N = list(map(int, input().split()))
    arr = list(map(int, input().split()))

# 인접리스트
    adjl = [[] for _ in range(100)] #adjl[i] 행(번호) i에 인접한 정점번호
    for i in range(N):
        n1, n2 = arr[i*2], arr[i*2+1]
    # 위 두 줄을 다음과 같이 나타낼 수도 있다.
    # for i in range(0, N, 2):
    #     n1, n2 = arr[i], arr[i+2]
        adjl[n1].append(n2)

    # print(adjl)

    result = 0 # 결과변수 초기화. 목표 노드에 도달하지 못하면 여전히 0이 되도록
    stack = [0] # 탐색을 시작할 노드를 스택에 넣습니다.
    node = nxt_node = 0

    while stack and nxt_node != 99: # stack이 비어있지 않고, 목표 노드에 도달하지 않았다면
        node = stack.pop() # 스택에서 노드를 하나 꺼내 탐색을 진행합니다.
        for nxt_node in adjl[node]: # 현재 노드에 연결된 다음 노드를 탐색
            if nxt_node == 99:
                result = 1
                break

            else:
                stack.append(nxt_node)

    print(f'#{tc} {result}')