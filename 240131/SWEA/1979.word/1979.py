T = int(input())

for t in range(1, T+1):
    N, K = list(map(int, input().split()))
    array = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        a =''.join(str(s) for s in arr)
        array.append(a)
    print(array)
    #arr = [list(''.join(input().split())) for _ in range(N)]
    # a = ''.join(arr)
    #print(arr)

#     result = 0
#
#     for i in range(N):
#         print(a)
# # 행을 str으로 바꾸어 0을 구분자로 split. 다시 list에 담아서 len이 K면 result+=1















    # result = 0
    #
    # # 행에서 연속된 1의 갯수 찾기
    # for i in range(N):
    #     counts = 0
    #     for j in range(N):    # (0,0), (0,1), (0,2)...
    #         if arr[i][j] == 1:
    #             counts += 1
    #         else: # 1이 아닌 수가 나오면 그 전까지 3이었을 경우 result값 1개 오르고, counts 재카운트
    #             if counts == K:
    #                 result +=1
    #             counts = 0
    #     if counts == K:
    #         result += 1
    #
    # # 열에서 연속된 1의 갯수 찾기
    # for j in range(N):
    #     counts = 0
    #     for i in range(N):
    #         if arr[i][j] == 1:
    #             counts += 1
    #         else:
    #             if counts == K:
    #                 result +=1
    #             counts = 0
    #     if counts == K:
    #         result += 1

    # print(f'#{t} {result}')