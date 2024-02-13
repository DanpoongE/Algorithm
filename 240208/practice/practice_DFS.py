'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(i, V): # 방문하는 정점 번호i        에 연결된 노드 나타내는 함수인듯 / 시작i, 마지막 V
    visited = [0]*(V+1) # 방문한 num
    stack = []          # visited, stack 생성 및 초기화

    ## 방문기록을 stack에 안 쌓고 재귀로 푸는 법
    # visitied[i] = 1 방문표시
    # print(i) 출력
    ## i에 인접하고 방문안한 w
    # for w in adjl[i]:
    #     if visited[w]==0:
    #         dfs(w, V)

    visited[i] = 1      # 시작점 방문
    print(i)            # 정점에서 할 일
    while True:         # 탐색
        for w in adjl[i]:
            if visited[w] == 0:  # 현재 방문한 정점에서 인접하고 방문안한 정점이 있으면 (조건1)
                stack.append(i)  # push(i), i를 지나서
                i = w
                visited[i] = 1   # 방문해서 할 일
                print(i)
                break
        else:                   # 현재 방문 위치가 막장이면
            if stack:              # 스택이 비어있지 않으면 거기로 가야지.
                i = stack.pop()
            else:                   # 스택이 비어있으면
                break               # 끝!
    return  # 함수니까 return!


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] #adjl[i] 행(번호) i에 인접한 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)     # 양방향 연결일 때
dfs(1, V)