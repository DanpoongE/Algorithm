'''
3
1 2 3
4 5 6
7 8 9
'''

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr2 = [[0]*N for _ in range(N)]
# # 잘못된 2차원 배열 ( 얕은 복사 )
# arr3 = [[0]*N]*N #-> 행렬이 되긴 하는데 얕은 복사라 arr3[m][m]일 때 전부 바뀜
# print(arr)

arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        print(arr[i][j])