from collections import deque

N, K = map(int, input().split())

to_go = deque()
to_go.append(N)
visited = [0] * 100001
visited[N] = 1
cnt = 0
now = N

while to_go:
    if visited[K] == 1:
        print(cnt)
        break

    cnt += 1
    for _ in range(len(to_go)):
        now = to_go.popleft()
        if 0 <= now - 1 <= 100000:
            if visited[now - 1] == 0:
                to_go.append(now - 1)
                visited[now - 1] = 1
        if 0 <= now + 1 <= 100000:
            if visited[now + 1] == 0:
                to_go.append(now + 1)
                visited[now + 1] = 1
        if 0 <= now * 2 <= 100000:
            if visited[now * 2] == 0:
                to_go.append(now * 2)
                visited[now * 2] = 1