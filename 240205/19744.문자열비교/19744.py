T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} 0')

