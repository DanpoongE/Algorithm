T = int(input())

def binary_search(bookpage, key):
    start = 0
    end = bookpage
    count = 0
    while start <= end:
        middle = int((start + end) / 2) # 중간값은 더해서 2로 나눠요
        if middle == key:           # 중간값이 key라면?
            count += 1              # 럭키한 당신! count1로 끝납니당
            return count
        elif middle < key:          # 아니라구요? 찾는 값이 middle보다 크면
            count += 1
            start = middle      # 시작 지점을 middle로 다시 잡을게요!
        else:
            count += 1
            end = middle

for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))

    count_A = binary_search(P, A)
    count_B = binary_search(P, B)

    if count_A == count_B:
        result = 0
    elif count_A < count_B:
        result = 'A'
    else:
        result = 'B'

    print(f'#{tc} {result}')