from heapq import heappush, heappop

def prim(start):
    visited= [0] * N # V는 끝점이지 전체 길이가 아님.
    edges = [(0, start)]    # 가중치 반영해서 넣기 위해 heap 도입
    mst_cost = 0            # 최소 신장 트리의 비용

    while edges:
        weight, node = heappop(edges)   # 가장 가중치가 작은 간선을 가져옴
        # 항상 최적인 간선이 아니라 아직 처리되지 않은 친구들
        if visited[node]:   # 방문을 했다면?
            continue
        visited[node] = 1   # 방문 처리
        mst_cost += weight  # mst에 해당 가중치를 더함
        for new_node, new_cost in graph[node]:
            if visited[new_node]:
                continue
            # 가중치, 이동할 노드 순으로 tuple을 만들어서 처리
            heappush(edges, (new_cost, new_node))

    return mst_cost


T= int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # V == 가장 마지막 노드 번호
    N = V + 1   # 전체 노드의 개수
    graph = [[] for _ in range(N)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
