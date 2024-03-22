T = int(input())

def merge_sort(arr):
    global answer
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    l = 0   #left 탐색할 인덱스
    r = 0   #right 탐색할 인덱스
    i = 0   # 병합된 리스트에 넣어줄 인덱스

    if left[-1] > right[-1]:
        answer += 1

    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1

        else:
            arr[i] =  right[r]
            r += 1
        i += 1

for tc in range(1, T + 1):
    print(f'#{tc}', end= ' ')
    answer = 0
    print(answer)
