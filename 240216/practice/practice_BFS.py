'''
V E : V 1~V번까지 V개의 정점. E개의 간선
E개의 간선정보

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, N): # 시작정점 s, 노드개수 N
    q = []                  # 큐
    visited = [0]*(N+1)     # visited
    q.append(s)             # 시작점 enqueue
    visited[s] = 1          # 방문표시

    while q:                # 큐가 비워질 때까지...(남은 정점이 있으면)
        t = q.pop(0)         # 앞에 있는 노드 pop
        print(t)            # dequeue되는 순서대로 출력하려구

        for i in adjl[t]:           # t에 인접한 애들 하나씩 꺼내볼래?
            if visited[i] ==0:      # 만약 인접 정점이 방문한 곳이 아니라면
                q.append(i)         # 큐에 enqueue
                visited[i] = visited[t] + 1 # visited에 넣고 이전 노드 방문값에 +1
    print(visited)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]
        adjl[n1].append(n2)
        adjl[n2].append(n1) # 무향그래프, 양향그래프
    S, G =  map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')
