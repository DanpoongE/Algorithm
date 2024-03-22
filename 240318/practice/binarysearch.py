arr = [23, 1, 9, 32, 975, 4331, 234556, 293, 89]
#1. 정렬
arr.sort()

# #2. 반복문으로 이진 탐색하기
# def binarySearch(target):
#     low = 0
#     high = len(arr) - 1
#
#     #탐색횟수
#     cnt = 0
#
#     # 해당 숫자를 찾으면 종료하거나(return을 통해 종료) 더 이상 쪼갤 수 없을 때까지
#     while low <= high:
#         mid = (low + high) // 2
#         cnt += 1
#
#         # 가운데 숫자가 정답이면 mid를 리턴하고 종료.
#         if arr[mid] == target:
#             return mid, cnt
#         elif arr[mid] > target:
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1

#3. 재귀함수로 구현하기
def binarysearch(target, low, high):
    # 기저조건
    if low > high:
        return -1
    # 다음 재귀 들어가기 전에 무엇을 해야할까? => 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid
    # 다음 재귀 함수 호출 (파라미터)
    if target < arr[mid]:
        return binarysearch(target, low, mid - 1)
    elif target > arr[mid]:
        return binarysearch(target, mid + 1, high)

    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?
print(arr)
print(binarysearch(32, 0, len(arr) - 1))
print(binarysearch(222, 0, len(arr) - 1))