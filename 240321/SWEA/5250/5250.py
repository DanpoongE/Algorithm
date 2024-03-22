from heapq import heappop, heappush

def dijkstra():
    distances = [[float('inf')] * N for _ in range(N)]
    distances[0][0] = 0 # 시작점 비용 0
    pq = [(0, 0, 0)]    # (비용, i, j)

    while pq:
        cost, i, j = heappop(pq)

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj

            if not (0 <= ni < N and 0 <= nj < N):
                continue
            h = arr[ni][nj] - arr[i][j]
            next_cost = 1 + max(0, h)       # 오르막 반영
            if distances[ni][nj] > cost + next_cost:
                # 갱신이 가능하다면
                distances[ni][nj] = cost + next_cost

                return 


T= int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    