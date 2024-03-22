# 인접 리스트 DFS
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    []
]
# 갈 수 있는 곳만 저장해뒀기 때문에 인접행렬dfs와 달리 반복문이 필요하지 않다.
visited = [0] * 5
path = []

def DFS(now):
    for to in graph[now]:

        if visited[to]: # 이미 방문했다면
            continue

        visited[to] = 1 # 방문표시
        path.append(to) # 간 길 담고
        DFS(to)

# 출발점 초기화, 호출 전 작업 시작
visited[0] = 1
path.append(0)
DFS(0)
print(path)



# ################ 인접행렬 DFS 재귀로 풀기 ###############
#
# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1],
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0],
# ]
#
# visited = [0] * 5
#
# def dfs(now):
#     # 기저 조건 => 지금 문제에선 없다. 재귀 호출 시 조건문이 기저 조건 역할을 해 줌.
#
#     # 다음 재귀 함수 호출 전
#     visited[now] = 1
#     print(now, end=' ')
#
#
#     # 다음 재귀 호출 == dfs: 현재 노드에서 갈 수 있는 다른 노드 확인
#     for to in range(5):
#         if graph[now][to] == 0: # 만약 갈 수 없다면
#             continue
#
#         if visited[to]: # 이미 방문했다면
#             continue
#
#         dfs(to)
#     # 돌아왔을 때 작업
#
# dfs(0)