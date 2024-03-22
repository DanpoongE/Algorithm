#1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자.
# 전체 간선 정보를 저장해서 가중치 순으로 sort

#2. 방문 처리. !!! 이때 사이클이 발생하면 안된다 !!!
# 이때 union-find 알고리즘이 활용.
def find_set(x):
    if parents[x] == x:
        return

    parents[x] = find_set(parents[x]) # 경로 압축
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 pass
    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())

edges = []  # 간선 정보 모두 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
edges.sort(key=lambda x: x[2])  # 가중치를 기준으로 정렬.
parents = [i for i in range(V)] # 대표자 배열

# MST 완성 = 간선의 개수가 V-1일 때.
cnt = 0

sum_weight = 0

# 간선들을 가중치 낮은 순서로 확인
for s, e, w in edges:
    # 사이클이 발생 == 이미 같은 집합에 속해 있다면 pass
    if find_set(s) == find_set(e):
        continue

    cnt += 1    # 선택할 때 cnt 올려주고
    # 사이클이 없으면, 방문 처리
    union(s, e)
    sum_weight += w

    if cnt == V:    # MST 완성! 간선의 개수 == V - 1
        break