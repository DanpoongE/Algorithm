def make_set(n):
    # 스스로가 부모 노드인 구조
    parents = [i for i in range(n+1)]
    return parents

parents = make_set(6)   # 처음 만들 때는 스스로가 스스로의 부모노드

def find_set(x):    # 대표자를 찾는 로직
    if parents[x] == x: # 스스로가 부모인 경우
        return x
    return find_set(parents[x])

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 집합을 대표할 수 있는 값을 찾아서 비교함
    if rep_x == rep_y:
        return # 이미 같은 집합임

    if rep_x < rep_y:   # 집합x의 대표가 더 작은 루트노드일 때
        parents[rep_y] = rep_x  # 그냥 y집합을 x집합에 붙여주기
    else:
        parents[rep_x] = rep_y
    print('union', parents)