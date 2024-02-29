# 중복 순열 구현하기

path = []
N = 3       # 주사위 개수를 밖으로 빼서 정의해줄수도 있음. 
def dice(x):
    if x == N + 1:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        dice(x + 1)
        path.pop()

dice(1)


# # 순열 구현하기
# path = []
# used = [False] * 100
#
# def dice(N, x = 1):
#     if x == N + 1:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         if used[i] == True: continue
#
#         path.append(i)
#         used[i] = True
#         dice(N, x + 1)
#         path.pop()
#         used[i] = False
#
# dice(3)