import sys
sys.stdin = open('5014.txt')
from collections import deque

def bfs(num, level):
    if num == G:
        print(level)
        return

    path.append(num)
    if num + U not in path:
        to_go.append(num + U)
    if num - D not in path:
        to_go.append(num - D)

F, S, G, U, D = map(int, input().split())
path = []
to_go = deque()

