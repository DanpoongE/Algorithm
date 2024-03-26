from itertools import combinations
import copy

def is_safe(arr, D, W):
    test = 'safe'
    global result
    for c in range(W):  # 열 하나씩 검토
        col_lst = []
        for r in range(D):
            col_lst.append(arr[r][c])
        col_str = ''.join(map(str, col_lst))  # 열 int -> str

        if standardA in col_str:            # A가 연속되면 safe이므로 break
            continue
        elif standardB in col_str:          # B가 연속되면 safe이므로 break
            continue
        else:                               # 안전조건에 한 열이라도 부합하지 않으면
            result = 'unsafe'
            return result
    return test                             # 다 통과시 안전함


T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    test_arr = copy.deepcopy(arr)
    r_lst = [n for n in range(D)]
    ans = 0
    standardA = '0' * K
    standardB = '1' * K
    result = 'unsafe'

    if is_safe(arr, D, W) == 'safe':        # 주입 안해도 통과
        print(f'#{tc}', ans)

    else:
        # while is_safe(arr, D, W) != 'safe':
        for k in range(1, D + 1):       # 주입할 줄의 개수. 1줄, 2줄...
            inject_lst = [i for i in combinations(r_lst, k)] # 주입할 줄을 튜플로 담은 리스트
            flag = 0

            for nums in inject_lst:
                test_arr = arr
                for rows in nums:
                    test_arr[rows] = [0] * W     # A 약물 주입

                if is_safe(arr, D, W) == 'safe': # 안전검사 통과하면
                    flag = 1
                    break

                # A 약물 주입한 결과 통과 못했으면
                test_arr = arr # arr 초기화
                for rows in nums:
                    test_arr[rows] = [1] * W     # B 약물 주입
                if is_safe(arr, D, W) == 'safe':    # 안전검사 통과하면
                    flag = 1
                    break

            # if flag == 1:
                print(f'#{tc}', k)
                break






    # for c in range(W):          # 열을 기준으로 탐색
    #     A = 0
    #     B = 0
    #     for r in range(D):
    #         if A > 0 and arr[r][c] == 0:  # 이전에 A였고 이번에도 A 약품이면
    #             A += 1
    #             if r == D - 1:              # 마지막 행이면
    #                 checkboard[c].append(A)
    #         elif A > 0 and arr[r][c] == 1:  # 이전엔 A였으나 이번엔 B라면
    #             checkboard[c].append(A)
    #             A = 0   # A 초기화
    #             B += 1
    #             if r == D - 1:              # 마지막 행이면
    #                 checkboard[c].append(B)
    #
    #         elif B > 0 and arr[r][c] == 1:  # 이전에 B였고 이번에도 B라면
    #             B += 1
    #             if r == D - 1:
    #                 checkboard[c].append(B)
    #         elif B > 0 and arr[r][c] == 0: # 이전엔 B였으나 이번엔 A라면
    #             checkboard[c].append(B)
    #             B = 0   # B 초기화
    #             A += 1
    #             if r == D - 1:              # 마지막 행이면
    #                 checkboard[c].append(A)
    #
    #         elif r == 0 and arr[r][c] == 0:  # 처음 A 약품이면
    #             A += 1
    #         elif r == 0 and arr[r][c] == 1:  # 처음 B 약품이면
    #             B += 1
    #
    # # 만약 모든 COL에 K 이상 숫자가 있으면 CNT = 0
    # standard = K
    # for col in checkboard:
    #     if
    #
    # # 아니라면 약품 주입해야 함.
    # print(checkboard)
