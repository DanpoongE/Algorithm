T = int(input())

for x in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    #N=손님수 M=초 K=붕어빵수
    customers = list(map(int, input().split()))
    customers.sort()
    flag = True
    for i in range(len(customers)):
        ready = (customers[i] // M) * K
        sold = i
        remain = ready - sold

        if remain > 0: continue

        else:
            flag = False
            print(f'#{x} Impossible')
            break
    if flag == True:
        print(f'#{x} Possible')
