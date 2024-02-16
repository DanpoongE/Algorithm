from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    adjl = [[] for __ in range(V+1)]        # 인접노드 리스트
    visited = [0]*(V+1)                  # 방문 기록
    q = deque()                             # 다음번 갈 노드
    distance = [0]*(V+1)

    for _ in range(E):
        a, b = list(map(int, input().split()))
        adjl[a].append(b)
        adjl[b].append(a)   # 양방향 노드

    # 인접 노드 다 기록하면 출발노드S와 도착노드G 주어짐
    S, G = list(map(int, input().split()))

    # 출발 노드 q에 기록, visited 기록
    q.append(S)
    visited[S] = 1
    distance[S] = 0

    while q:    # 갈 곳이 없을 때까지
        node = q.popleft()  # q에서 첫번째 노드 꺼내서
        for adj in adjl[node]:  # 해당 노드와 인접한 노드 번호 찾고
            if visited[adj] == 0: # 인접한 노드를 방문한 적이 없다면
                q.append(adj)       # q에 넣고
                visited[adj] = 1    # 방문표시
                distance[adj] = distance[node] + 1

            if adj == G:    # 만일 인접한 노드가 G라면
                q.clear()

    print(f'#{tc} {distance[G]}')
