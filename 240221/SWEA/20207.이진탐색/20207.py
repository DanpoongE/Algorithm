# # 중위순회
# def inorder(n):
#     global num
#
#     # 왼쪽 자식 확인
#     if n <= N: # 범위를 넘어서지 않을 때, N =6
#         inorder(n*2) # 왼쪽 자식
#         tree[n] = num
#         num += 1
#
#         inorder(n*2+1)  # 오른쪽 자식
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0] * (N+1)
#     num = 1
#     inorder(1)
#     print(f'#{tc} {tree[1]} {tree[N//2]}')




# 중위순회
def inorder(n):

    # 왼쪽 자식 확인
    if n <= N: # 범위를 넘어서지 않을 때, N =6
        inorder(n*2) # 왼쪽 자식
        tree[n] = arr.pop()

        inorder(n*2+1)  # 오른쪽 자식

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    arr = list(range(N, 0, -1))
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')




        #이제 오른쪽.
    #     while tree[last_idx*2 + 1] and [last_idx] > tree[last_idx*2 + 1]: # 오른쪽 자식 노드가 있고
    #         tree[last_idx], tree[last_idx*2 + 1] = tree[last_idx*2 + 1], tree[last_idx]
    #
    # print(tree)