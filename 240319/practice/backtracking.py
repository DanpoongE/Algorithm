# 중복된 순열
# 1~3까지 있을 때 길이가 3인 중복순열 만들어보자

# <<재귀 함수 팁>>
# 구조를 먼저 잡고 -> 필요한 변수를 전역변수나 매개변수로 넣어준다.
# 들어가기 전
# 다음 재귀 호출
# 갔다와서 할 로직

arr = [i for i in range(1, 4)]
path = [0] * len(arr)

def dfs(level):
    if level == 3:
        print(*path)
        return

    # path[level] = 1
    # dfs(level + 1)
    #
    # path[level] = 2
    # dfs(level + 1)
    #
    # path[level] = 3
    # dfs(level + 1)

    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level + 1)

dfs(0)