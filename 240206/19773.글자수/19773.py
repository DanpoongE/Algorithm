T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = input()

    N = len(str1)

    result = 0
    for i in range(N):

        if result < str2.count(str1[i]): # 현재 result 값보다 특정 문자를 센 값이 더 큰 경우
            result = str2.count(str1[i]) # result 값을 해당 수로 바꾼다

    print(f'#{tc} {result}')