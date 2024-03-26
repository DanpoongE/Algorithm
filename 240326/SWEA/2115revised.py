import sys
sys.stdin = open('2115.txt')
from itertools import combinations

def cost_idx(lst):
    cost_idx = []
    for r in range(N): 
        for c in range(N - M + 1):
            select = lst[r][c:c + M]
            if sum(select) <= C:    # 선택한 벌통에 든 꿀이 최대치를 넘지 않는다면
                val = 0
                for nums in select:
                    val += nums*nums
                cost_idx.append([val, (r, c)])
            
            else: # 선택한 벌통에 든 꿀이 최대치를 넘는다면
                max_val = 0
                for length in range(M - 1, 0, -1):
                    for combi in combinations(select, length):
                        sum_honey = 0
                        if sum(combi) <= C:
                            for honey in combi:
                                sum_honey += honey*honey
                            if sum_honey > max_val:
                                max_val = sum_honey
                cost_idx.append([max_val, (r, c)])
    cost_idx.sort()
    # print(cost_idx)
    pick_two(cost_idx)

def pick_two(lst):
    ans = 0
    worker1 = lst.pop()     # 첫번째 일꾼, 돈이 제일 높은 꿀통 선택
    worker2 = lst.pop()     # 두번째 일꾼, 돈이 두번째로 높은 꿀통 선택
    # print('worker1:', worker1[1], '/', 'worker2:', worker2[1])

    if worker2[1][0] != worker1[1][0]:  # 두명이 선택한 꿀통이 같은 행이 아니라면
        ans = worker1[0] + worker2[0]
        print(ans)

    else:  # 두명이 선택한 꿀통이 같은 행에서 뽑은 거라면
        while is_overlap(worker1, worker2): # 겹치는 경우
            worker2 = lst.pop()             # 2번 일꾼 다시뽑기
        ans = worker1[0] + worker2[0]
        print(ans)
        
def is_overlap(arg1, arg2):
    if arg1[1][0] != arg2[1][0]:
        return False
    big = max(arg1[1][1], arg2[1][1])
    small = min(arg1[1][1], arg2[1][1])
    if big < small + M:     # 겹치는 경우
        return True
    else:
        return False


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', end=' ')
    cost_idx(arr)
