print()
def f(i, k, t): # k개의 원소를 가진 배열A에서 합이 t인 부분집합을 찾기
    if i==k:    # 모든 원소에 대해 결정하면???? 이게 무슨 말?
        ss = 0  # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:  #A[j]가 포함된 경우
                # print(A[j], end=' ')
                ss += A[j]
        if ss==t:
            for j in range(k):
                if bit[j]:  # A[j]가 포함된 경우
                    print(A[j], end=' ')
            print()
        # print(ss)
    else:
        for j in range(1, -1, -1): # 1부터 넣어주고 싶다면
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1 # 갈림길이 두개였기 때문에
        # f(i+1, k)   # 다음 원소를 결정하러 가봐
        # bit[i] = 0
        # f(i+1, k)


N = 3
A = [1, 2, 3]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 3)






# def f(i, k, s, t):
#     if s==t:
#         for j in range(k):
#             if bit[j]:
#                 print(A[j], end=' ')
#         print() # 부분집합 출력
#     elif i==k:  # 모든 원소를 고려했으나 s!=t
#         return
#     elif s > t: # 고려한 원소의 합이 t보다 큰 경우
#         return
#     else:   # 그렇지 않으면 좀 만들어볼래?
#         bit[i] = 1
#         f(i+1 , k, s+A[i], t)
#         bit[i] = 0
#         f(i+1, k, s, t)
