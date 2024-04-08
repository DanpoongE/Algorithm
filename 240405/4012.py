def taste(combi_X):
    combis = combinations(combi_X, 2)
    taste_X = 0

    for combi in combis:
        taste_X += arr[combi[0]][combi[1]]
        taste_X += arr[combi[1]][combi[0]]

    return taste_X

from itertools import combinations, permutations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # 식재료의 수
    ingredients = set(range(N))
    arr = [list(map(int, input().split())) for _ in range(N)]   # 시너지 테이블
    combi_list = list(combinations(range(N), N // 2))
    ans = float('inf')

    for combi_A in combi_list:  # A메뉴 만들 재료 조합
        combi_B = tuple(ingredients - set(combi_A))
        taste_A = taste(combi_A)
        taste_B = taste(combi_B)
        taste_gap = abs(taste_A - taste_B)

        if taste_gap < ans:
            ans = taste_gap

    print(f'#{tc}', ans)


# for combi_A in combi_list: # A메뉴 만들 재료 조합
#     for combi_B in combi_list: #B메뉴 만들 재료 조합
#         if combi_list.index(combi_A) < combi_list.index(combi_B):   # 후순위인 B의 index가 더 큼. 중복방지
#             if len(set(combi_A + combi_B)) == N: # 식재료들끼리 겹치지 않는다면
#                 taste_A = taste(combi_A)
#                 taste_B = taste(combi_B)
#                 taste_gap = abs(taste_A - taste_B)
#
#                 if taste_gap < ans:
#                     ans = taste_gap
