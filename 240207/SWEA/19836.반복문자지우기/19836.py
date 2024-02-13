T = int(input())

for tc in range(1, T+1):
    s = input()

    temp_s = []
    for x in s:
        if temp_s and temp_s[-1] == x:
            temp_s.pop()

        else:
            temp_s.append(x)

        result = len(temp_s)

    print(f'#{tc} {result}')