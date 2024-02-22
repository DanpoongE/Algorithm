def inorder(n):
    # 왼쪽 자식 노드가 있다면 거기로.
    if left[n]:
        inorder(left[n])

    if right[n]:
        result.append(node_info[n])
        inorder(right[n])

    else:
        result.append(node_info[n])
    # 부모 노드로 어떻게 돌아갈 것인지 신경쓸 필요가 없다.
    # 재귀를 통해 가지 않은 나머지 가지를 다음 번에 실행하기 때문!

T = 10

for tc in range(1, T+1):
    N = int(input())
    node_info = [0]*(N+1)      # 해당 정점의 문자 저장할 빈 리스트
    left = [0]*(N+1)    # 부모 인덱스 기준 왼쪽 자식 번호 저장
    right = [0]*(N+1)   # 부모 인덱스 기준 오른쪽 자식 번호 저장
    parent = [0]*(N+1)  # 자식 인덱스 기준 부모 번호 저장

    result = []         # 답을 저장할 빈 리스트 하나 생성

    # 시작!
    for _ in range(N):
        arr = input().split()
        node = int(arr[0])
        node_info[node] = arr[1]        # 정점의 문자들 저장.

        if len(arr) >= 3:      # 왼쪽 자식 노드가 있다면
            left_child = int(arr[2])
            left[node] = left_child   # 부모 인덱스 기준 왼쪽 자식 번호 저장
            parent[left_child] = node   # 자식 인덱스 기준 부모 번호 저장

        if len(arr) == 4:      # 오른쪽 자식 노드가 있다면
            right_child = int(arr[3])
            right[node] = right_child   # 부모 인덱스 기준 오른쪽 자식 번호 저장
            parent[right_child] = node  # 자식 인덱스 기준 부모 번호 저장

    inorder(1)      # 늘 1번 노드부터 시작
    print(f'#{tc}', ''.join(result))
