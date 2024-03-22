from collections import deque

# 인접 리스트 BFS
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]

visited = [0] * 5

def bfs(start):
    # 시작 노드를 덱에 추가 + 방문 표시
    q = deque(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        print(now, end= ' ')

        # 갈 수 있는 곳을 체크 후 넣어주기
        for to in graph[now]:
            if visited[to]:         # 방문했다면 1로 표시되어 true가 됨
                continue

            visited[to] = 1
            q.append(to)

bfs(0)