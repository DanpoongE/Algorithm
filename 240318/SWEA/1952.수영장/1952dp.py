T = int(input())
for t in range(T):
    day_per, month_per, month3_per, year_per = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    dp = [0] * 13

    for i in range(1, 13):
        dp[i] = min(month_per, arr[i] * day_per) + dp[i - 1]

        if i >= 3:
            dp[i] = min(dp[i - 3] + month3_per, dp[i])

    print(f'#{t + 1} {min(dp[12], year_per)}')