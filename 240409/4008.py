from itertools import permutations
import math

def cal_in_order(set):
    max_val = -100000000
    min_val = 100000000

    for k in range(len(set)):       # 전체 연산 횟수
        ans = 0
        for c in range(N - 1):
            if c == 0:
                if set[k][c] == '+':
                    ans += nums[c] + nums[c + 1]
                elif set[k][c] == '-':
                    ans += nums[c] - nums[c + 1]
                elif set[k][c] == '*':
                    ans += nums[c] * nums[c + 1]
                elif set[k][c] == '/':
                    ans += math.trunc(nums[c] / nums[c + 1])
            else:
                if set[k][c] == '+':
                    ans += nums[c + 1]
                elif set[k][c] == '-':
                    ans -= nums[c + 1]
                elif set[k][c] == '*':
                    ans *= nums[c + 1]
                elif set[k][c] == '/':
                    ans = math.trunc(ans / nums[c + 1])
        if ans > max_val:
            max_val = ans
        if ans < min_val:
            min_val = ans

    return max_val - min_val

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cal = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cal_signs = []
    cal_dict = {0 : '+', 1 : '-', 2 : '*', 3 :'/'}

    for _ in range(cal[0]):
        cal_signs.append(cal_dict[0])
    for _ in range(cal[1]):
        cal_signs.append(cal_dict[1])
    for _ in range(cal[2]):
        cal_signs.append(cal_dict[2])
    for _ in range(cal[3]):
        cal_signs.append(cal_dict[3])

    cals_set = list(set(permutations(cal_signs, N - 1)))

    print(f'#{tc}', cal_in_order(cals_set))