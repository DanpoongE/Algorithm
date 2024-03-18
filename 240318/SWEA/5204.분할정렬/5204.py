def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 리스트 2분할
    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    # 2분할한 리스트를 각각 merge sort 진행
    left = merge_sort(left_part)
    right = merge_sort(right_part)
    return merge(left, right)

def merge(left, right):
    global ans
    l, r = 0, 0
    sorted_lst = []

    while l < len(left) and r < len(right):
        if l == 0 and r == 0 and left[-1] > right[-1]:
            ans += 1

        if left[l] < right[r]:
            sorted_lst.append(left[l])
            l += 1
        else:
            sorted_lst.append(right[r])
            r += 1

    while l < len(left):
        sorted_lst.append(left[l])
        l += 1
    while r < len(right):
        sorted_lst.append(right[r])
        r += 1
    return sorted_lst

TC = int(input())

for T in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    print(f'#{T}', merge_sort(lst)[N//2], ans)