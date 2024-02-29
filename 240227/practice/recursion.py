'''
012345543210을 재귀호출을 이용하여 구현하기
'''

def nums_up(n):
    if n == 6:
        return

    print(n, end=' ')
    nums_up(n + 1)
    print(n, end=' ')

# def nums_down(n):
#     if n < 0:
#         return
#     print(n)
#     nums_down(n-1)


nums_up(0)          # 함수 내부에 print가 있으면 함수 호출만으로 print가능!
# print(nums_down(5))