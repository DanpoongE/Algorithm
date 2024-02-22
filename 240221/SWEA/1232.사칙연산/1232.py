T = 10
for t in range(1, T+1):
    N = int(input())        # 노드의 개수
    tree = [0]           # 인덱스를 노드 번호로 하는 key 값 담을 리스트. index0은 0
    p = [0] * (N+2)             # 인덱스를 자식 노드 번호로 하는 부모 노드 번호 저장 리스트

    # 트리 만들기
    for _ in range(N):
        node_info = list(input().split())
        # 정점 번호, 연산자, 왼쪽 자식 정점 번호, 오른쪽 자식 정점 번호
        # 정점 번호, 양의 정수

        node = int(node_info[0])
        tree.insert(node, node_info[1])

        # 부모 노드 번호 저장하기
        if len(node_info) > 2:  # 자식이 하나인 경우는 없으니까
            p[int(node_info[2])] = node
            p[int(node_info[3])] = node

    last_idx = len(tree) - 1            # 마지막 인덱스


    while last_idx > 1:                # 마지막 인덱스가 1이 될 때까지
        if tree[p[last_idx]] == '+':
            tree[p[last_idx]] = float(tree[last_idx - 1]) + float(tree[last_idx])

        elif tree[p[last_idx]] == '-':
            tree[p[last_idx]] = float(tree[last_idx - 1]) - float(tree[last_idx])

        elif tree[p[last_idx]] == '*':
            tree[p[last_idx]] = float(tree[last_idx - 1]) * float(tree[last_idx])

        else:   # 나눗셈이면
            tree[p[last_idx]] = float(tree[last_idx - 1]) / float(tree[last_idx])

        last_idx -= 2

    print(f'#{t} {int(tree[1])}')
