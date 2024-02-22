T = int(input())

for tc in range(1, T+1):
    #N:노드개수, M:리프노드개수, L:목표노드
    N, M, L = list(map(int, input().split()))
    node_info = [0] * (N+1)     # 해당 노드의 인덱스에 저장된 값 저장
    leaves = []

    for _ in range(M):
        leaf_node, num = list(map(int, input().split()))
        leaves.append(leaf_node)
        node_info[leaf_node] = num

    start = max(leaves)         # 리프 노드 중 가장 큰 수 = 시작점

    if start % 2 == 0:          # 시작 지점이 짝수라면
        node_info[start // 2] = node_info[start]
        start = start - 2

    else:                       # 시작 지점이 홀수라면
        node_info[(start-1)//2] = node_info[(start-1)] + node_info[start]
        start = start - 2

    while start > 1:       # 루트 직전까지
        if start % 2 == 0: # 시작 노드가 짝수라면
            node_info[start // 2] = node_info[start] + node_info[(start+1)]
            start = start - 2
        else:   # 시작 노드가 홀수라면
            node_info[(start - 1) // 2] = node_info[(start - 1)] + node_info[start]
            start = start - 2

    # 마지막으로 루트 노드 값
    node_info[1] = node_info[2] + node_info[3]

    print(f'#{tc} {node_info[L]}')

