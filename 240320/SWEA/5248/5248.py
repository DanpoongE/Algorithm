T = int(input())  # 테스트 케이스의 수를 입력받습니다.

def find(x):
    if parent[x] == x:  # 자신이 루트 노드라면 자신을 반환합니다.
        return x
    # 경로 압축: 자신이 속한 집합의 루트 노드를 바로 부모 노드로 설정합니다.
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)  # x의 루트 노드
    root_y = find(y)  # y의 루트 노드

    # 동일한 루트 노드면 생략
    if root_x == root_y:
        return

    # 랭크가 더 높은 트리 아래에 랭크가 더 낮은 트리를 합칩니다.
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:  # 랭크가 같은 경우 한 쪽의 랭크를 1 증가시킵니다.
            rank[root_x] += 1

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))
    # subset 만들기
    parent = [i for i in range(N+1)]  # 각 노드의 부모 노드를 저장하는 리스트
    rank = [0 for _ in range(N+1)]  # 각 노드의 랭크를 저장하는 리스트

    for i in range(0, len(edges), 2):  # 간선 정보를 인접 행렬에 추가합니다.
        x, y = edges[i] - 1, edges[i+1] - 1
        union(x, y)  # x와 y를 같은 집합으로 합칩니다.

    # 각 노드의 루트 노드를 찾아 집합으로 만든 후 그 크기를 출력합니다.
    print(len(set([find(v) for v in range(N)])))