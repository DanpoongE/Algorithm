import sys
sys.stdin = open("1952.txt")

T = int(input())

for t in range(1, T + 1):
    costs = list(map(int, input().split()))
    schedule = list(map(int, input().split()))

    visit_month_index = []
    for i in range(12):
        if schedule[i] > 0:
            visit_month_index.append(i)
    visit_times = len(visit_month_index)

    #일일 이용권만 이용시 요금
    daily = costs[0] * sum(schedule)
    ans = daily

    #월간 이용권만 이용시 요금
    monthly = costs[1] * visit_times
    if monthly <= ans:
        ans = monthly

    #일일 + 월간 이용권 이용시 요금
    day_mon_mix = 0
    for d in visit_month_index: # 수영장에 1회 이상 방문하고
        if costs[0] * schedule[d] < costs[1]:   # 일일이용권이 더 싸면
            day_mon_mix += costs[0] * schedule[d]
        else:   # 월간이용권이 더 싸면
            day_mon_mix += costs[1]
    if day_mon_mix <= ans:
        ans = day_mon_mix

    # 3달 이용권만 이용시
    month3_ticket = 0
    for m in range(visit_times):
        if m == 0:
            startmonth = visit_month_index[m]
            month3_ticket += 1
        elif visit_month_index[m] - startmonth >= 3:
            month3_ticket += 1
            startmonth = visit_month_index[m]
    if month3_ticket * costs[2] <= ans:
        ans = month3_ticket * costs[2]

    # 3달 이용권 + day + mon
    mix_cost = 0
    if 4 <= visit_times <= 6:        # 3달 이용권은 한번만
        for idx in range(10): # 시작 인덱스로부터
            mix_cost = costs[2]
            for ii in range(12):
                if ii not in [idx, idx+1, idx+2]: # 연속 3달은 패스하고 일일권과 한달권 비교
                    if costs[0] * schedule[ii] <= costs[1]: # 일일권이 더 싸면
                        mix_cost += costs[0] * schedule[ii]
                    else:
                        mix_cost += costs[1]
            if mix_cost <= ans:
                ans = mix_cost
            else:
                mix_cost = 0

    elif 7 <= visit_times <= 9:      # 3달 이용권 최대 2번
        for idx in range(10):                   # 3달 이용권 1번 이용시
            mix_cost = costs[2]
            for ii in range(12):
                if ii not in [idx, idx+1, idx+2]:
                    # mix_cost += costs[2]
                    if costs[0] * schedule[ii] <= costs[1]: # 일일권이 더 싸면
                        mix_cost += costs[0] * schedule[ii]
                    else:
                        mix_cost += costs[1]
            if mix_cost <= ans:
                ans = mix_cost
            else:
                mix_cost = 0

        for idx in range(10):                   # 3달 이용권 2번 이용시
            mix_cost = costs[2]
            for idx2 in range(10):
                if idx2 not in [idx, idx+1, idx+2]:
                    mix_cost = costs[2] * 2
                    for idx3 in range(12):  # 일일이나 한달이용권
                        if idx3 not in [idx, idx + 1, idx + 2, idx2, idx2 + 1, idx2 + 2]:
                            if costs[0] * schedule[idx3] <= costs[1]: # 일일권이 더 싸면
                                mix_cost += costs[0] * schedule[idx3]
                            else:
                                mix_cost += costs[1]
                    if mix_cost <= ans:
                        ans = mix_cost
                    else:
                        mix_cost = 0

    elif 10 <= visit_times <= 12:
        for idx in range(10):                   # 3달 이용권 1번 이용시
            mix_cost = costs[2]
            for ii in range(12):
                if ii not in [idx, idx+1, idx+2]:
                    if costs[0] * schedule[ii] <= costs[1]: # 일일권이 더 싸면
                        mix_cost += costs[0] * schedule[ii]
                    else:
                        mix_cost += costs[1]
            if mix_cost <= ans:
                ans = mix_cost
            else:
                mix_cost = 0
        
        for idx in range(10):                   # 3달 이용권 2번 이용시
            mix_cost = costs[2]
            for idx2 in range(10):
                if idx2 not in [idx, idx+1, idx+2]:
                    mix_cost = costs[2] * 2
                    for idx3 in range(12):  # 일일이나 한달이용권
                        if idx3 not in [idx, idx + 1, idx + 2, idx2, idx2 + 1, idx2 + 2]:
                            if costs[0] * schedule[idx3] <= costs[1]: # 일일권이 더 싸면
                                mix_cost += costs[0] * schedule[idx3]
                            else:
                                mix_cost += costs[1]
                    if mix_cost <= ans:
                        ans = mix_cost
                    else:
                        mix_cost = 0

        for idx in range(10):               # 3달 이용권 3번 이용시
            mix_cost = costs[2]
            for idx2 in range(10):
                if idx2 not in [idx, idx + 1, idx + 2]:
                    mix_cost = costs [2] * 2
                    for idx3 in range(10):
                        if idx3 not in [idx, idx + 1, idx + 2, idx2, idx2 + 1, idx2 + 2]:
                            mix_cost = costs[2] * 3
                            for idx4 in range(12):
                                if idx4 not in [idx, idx2, idx3, idx+1, idx2+1, idx3+1, idx+2, idx2+2, idx3+2]:
                                    if costs[0] * schedule[idx4] <= costs[1]:
                                        mix_cost += costs[0] * schedule[idx4]
                                    else:
                                        mix_cost += costs[1]
                                        
                            if mix_cost <= ans:
                                ans = mix_cost
                            else:
                                mix_cost = 0

    # 1년 이용권 이용시
    if costs[3] <= ans:
        ans = costs[3]

    print(f'#{t} {ans}')