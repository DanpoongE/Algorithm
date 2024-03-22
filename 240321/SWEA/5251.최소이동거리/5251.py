from heapq import heappush, heappop

def dijkstra(start, end):
    heappush(pq, (0, start))        # 첫 시작지점 넣어주고
    distance[0] = 0             # 시작 노드 거리는 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:    # 이미 해당 노드까지의 거리가 dist보다 최소값이라면
            continue

        for adjs in adj_lst[now]:
            next = adjs[0]
            add_dist = adjs[1]
            new_dist = dist + add_dist

            if new_dist < distance[next]:    # 다음 노드까지의 거리 < 현재 기록된 거리
                distance[next] = new_dist
                heappush(pq, (new_dist, next))

    return distance[end]

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split()) # N == 노드 번호, E == 간선 개수
    INF = int(21e8)
    distance = [INF] * (N + 1)        # 노드 번호 0번부터 시작
    adj_lst = [[] for _ in range(N + 1)]    # 마지막 노드는 도착지이므로 인접리스트 필요 없으나 리스트 레인지 문제로.
    pq = []

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_lst[s].append([e, w])

    print(f'#{tc}', dijkstra(0, N))