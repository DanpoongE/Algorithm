def backtrack(n):
    global answer

    if n == total_change:
        answer = max(answer, int(''.join(num_list)))
        return

    for i in range(len_of_num - 1):
        for j in range(i + 1, len_of_num):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            if not memo.get((''.join(num_list), n)):
                backtrack(n + 1)
                memo[(''.join(num_list), n)] = True
            num_list[j], num_list[i] = num_list[i], num_list[j]


T = int(input())
for tc in range(1, T + 1):
    num, total_change = input().split()
    len_of_num = len(num)
    total_change = int(total_change)
    memo = {}
    num_list = list(num)
    answer = 0

    backtrack(0)
    print(f'#{tc} {answer}')