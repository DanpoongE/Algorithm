from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)
to_go = deque()

to_go.append(S)
visited[S] = 1

while to_go:
    start = to_go.popleft()

    if start == G:      # 목표층이면
        print(visited[G] - 1)
        break

    # 목표층이 아니면
    up = start + U
    down = start - D

    if 0 < up <= F:
        if visited[up] == 0:
            visited[up] = visited[start] + 1
            to_go.append(up)

    if 0 < down <= F:
        if visited[down] == 0:
            visited[down] = visited[start] + 1  # 버튼 누른 횟수 기록
            to_go.append(down)

if visited[G] == 0:
    print('use the stairs')




# while to_go:    # 갈 수 있는 층이 남아 있을 때까지
#     cnt += 1
#     for floors in range(len(to_go)):
#         start = to_go.popleft()
#         if start == G:
#             arrive = True
#             print(cnt - 1)
#             break
#         up = start + U
#         down = start - D
#
#         if up not in path:  # 갔던 층이 아니면
#             to_go.append(up)
#             path.append(up)
#
#         if down not in path:
#             if down > 0:   # 0 이하로 떨어지면 안봄
#                 to_go.append(down)
#                 path.append(down)
#
#     if arrive:
#         break
#
# if arrive == False:
#     print('use the stairs')