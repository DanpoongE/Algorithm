from heapq import heappush, heappop
def prim(start):
    pq = []         # 우선순위 큐. 덱과 같은 역할
    MST = [0] * V   # visited와 같은 역할

    # 최소 비용
    sum_weight = 0

    #시작점 추가
    #prim에서는 가중치가 낮으면 먼저 나와야 한다. -> 관리해야할 데이터: 가중치, 노드번호
    #두가지 정보 한번에 다루는 방법 1. class로 만들기(3개이상) 2. 튜플로 관리
    heappush(pq, (0, start))        #pq에 가중치가 낮은 순서대로 들어간다.

    while pq:
        weight, now = heappop(pq)

        # 방문했다면 continue. bfs에서는 없었던 부분!!!!
        if MST[now]:
            continue
            # 우선순위 큐의 특성상 더 먼거리로 돌아서 가는 방법이 큐에 저장되기 때문에
            # 기존에 이미 더 짧은 거리로 방문했다면, continue

        MST[now] = 1
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            if graph[now][to] == 0: # 못가면
                continue
            if MST[to]: # 이미 방문했다면
                continue

            heappush(pq, (graph[now][to], to))      #(가중치, 번호) 넣어주기



V, E = map(int, input().split())
# 인접 행렬로 저장

graph = [[0] * V for _ in range(V)] # 가중치 그래프
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w                 # s노드에서 시작해 e로 가는 간선의 가중치 w
    # 무방향 그래프
    graph[e][s] = w

print(graph)
