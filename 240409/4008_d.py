import math
def generate(chosen, used):
    global max_val, min_val

    if len(chosen) == N - 1:
        if calcul(chosen) > max_val:
            max_val = calcul(chosen)
        if calcul(chosen) < min_val:
            min_val = calcul(chosen)
        return

    for i in range(N - 1):
        if not used[i]:
            if i == 0 or cal_signs[i - 1] != cal_signs[i] or used[i - 1]:
                chosen.append(cal_signs[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

def calcul(lst):
    ans = nums[0]
    for c in range(N - 1):
        if lst[c] == '+':
            ans += nums[c + 1]
        elif lst[c] == '-':
            ans -= nums[c + 1]
        elif lst[c] == '*':
            ans *= nums[c + 1]
        elif lst[c] == '/':
            ans = math.trunc(ans / nums[c + 1])

    return ans


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cal = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    cal_signs = []
    cal_dict = {0 : ['+'], 1 : ['-'], 2 : ['*'], 3 : ['/']}
    cal_signs.extend(cal_dict[0] * cal[0])
    cal_signs.extend(cal_dict[1] * cal[1])
    cal_signs.extend(cal_dict[2] * cal[2])
    cal_signs.extend(cal_dict[3] * cal[3])

    used = [0] * (N - 1)
    max_val = -100000000
    min_val = 100000000

    generate([], used)

    print(f'#{tc} {max_val-min_val}')
