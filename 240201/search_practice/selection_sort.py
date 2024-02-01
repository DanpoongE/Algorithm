def selection_sort(a, N):
    for i in range(N-1):        # 구간시작 i, 2개 원소 남을때까지
        min_idx = i             # 구간의 최솟값 위치 min_dix, 첫 원소를 최소로 가정
        for j in range(i+1, N): # 구간의 실제 최솟값
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx] # 최솟값을 구간의 맨 앞으로 이동
    return

N = 5
arr = [1, 3, 2, 5, 4]
print(arr)  # 정렬 전
selection_sort(arr, N)
print(arr)  # 정렬 후


def my_sort(a, N):
    for i in range(N):
        minimum = min(a)
        if a[i] < minimum:
            a[i], minimum = minimum, a[i]
    return

N = 5
arr = [1, 3, 2, 5, 4]
print(arr)  # 정렬 전
my_sort(arr, N)
print(arr)  # 정렬 후