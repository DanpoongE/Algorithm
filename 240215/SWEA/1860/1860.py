# output = open('output (3).txt')
# ans = []
# for i in output:
#     ans.append(i.strip())
my_ans = []

T = int(input())

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split())) # N명, M초, K개
    arrival = list(map(int, input().split()))
    # 손님 오는 시간 오름차순으로 정리
    arrival.sort()


    # 진기가 붕어빵을 만들기 위해 필요한 최소 시간보다 더 빨리오는 손님이 있다면
    if arrival[0] < M:
        print(f'#{tc} Impossible') # 무조건 impossible.
        my_ans.append(f'#{tc} Impossible')

    # 모든 손님이 최소 시간보다 늦게 오고 진기가 만들어내는 붕어빵 수가 손님 수보다 많다면
    elif K >= N:
        print(f'#{tc} Possible') # 무조건 possible.
        my_ans.append(f'#{tc} Possible')


        # 모든 손님이 최소 시간보다 늦게 오나 진기가 한번에 만들어내는 붕어빵 수가 손님 수보다 적다면
    else:
        # 제일 늦게 오시는 손님 시간
        last = max(arrival)

        n = 1
        re = 'Possible'
        while M*n <= last and len(arrival) > K*n-1:
            if arrival[K*n-1] < M*n: # 붕어빵 cycle개수와 cycle상 마지막 손님 도착 시간 비교
                re = 'Impossible'
                break
                # my_ans.append(f'#{tc} Impossible')

            else:
                n += 1
        print(f'#{tc} {re}')
        my_ans.append(f'#{tc} Possible')


# for i in range(1000):
#     if ans[i] != my_ans[i]:
#         print(ans[i], my_ans[i])