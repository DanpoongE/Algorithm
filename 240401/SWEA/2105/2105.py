import sys
sys.stdin = open('2105.txt')

def dessert_tour(i, j):
    to_go = []
    to_go.append(i, j) # 시작점 

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

