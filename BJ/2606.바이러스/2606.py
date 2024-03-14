from collections import deque

N = int(input())
C = int(input())
networks = [[] for _ in range(N + 1)]
infected = [0] * (N + 1)

for _ in range(C):
    com1, com2 = list(map(int, input().split()))
    networks[com1].append(com2)
    networks[com2].append(com1)

virus = deque()
virus.append(1)
infected[1] = 1

ans = 0

while virus:
    host = virus.popleft()
    if host != 1:
        ans += 1

    for i in networks[host]:
        if infected[i] == 0:
            virus.append(i)
            infected[i] = 1

print(ans)
