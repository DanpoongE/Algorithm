import sys
sys.stdin = open('B2116input.txt')

N = int(input())
dice_arr = [list(map(int, input().split())) for _ in range(N)]
max_val = []        # 옆면 최대 숫자들
ans = 0

for s in range(6):      # 주사위 6면
    start_index = s

    if start_index == 0:
        side_index = [1, 2, 3, 4]
        up_index = 5
    elif start_index == 1:
        side_index = [0, 2, 4, 5]
        up_index = 3
    elif start_index == 2:
        side_index = [0, 1, 3, 5]
        up_index = 4
    elif start_index == 3:
        side_index = [0, 2, 4, 5]
        up_index = 1
    elif start_index == 4:
        side_index = [0, 1, 3, 5]
        up_index = 2
    elif start_index == 5:
        side_index = [1, 2, 3, 4]
        up_index = 0

    side_nums = []
    for idx in side_index:
        side_nums.append(dice_arr[0][idx])

    max_val.append(max(side_nums))

    for i in range(N - 1):  # 첫 주사위를 뺀 나머지 주사위개수
            # 이전 hidden 값의 idx와 마주보는 값 (위로 올라가는 값)
        next_idx = dice_arr[i + 1].index(dice_arr[i][up_index])

        if next_idx == 0:
            side_index = [1, 2, 3, 4]
            up_index = 5
            
            sside_nums = []
            for iidx in side_index:
                sside_nums.append(dice_arr[i + 1][iidx])

            max_val.append(max(sside_nums))
            
        elif next_idx == 1:
            side_index = [0, 2, 4, 5]
            up_index = 3
            
            sside_nums = []
            for iidx in side_index:
                sside_nums.append(dice_arr[i + 1][iidx])

            max_val.append(max(sside_nums))

        elif next_idx == 2:
            side_index = [0, 1, 3, 5]
            up_index = 4

            sside_nums = []
            for iidx in side_index:
                sside_nums.append(dice_arr[i + 1][iidx])

            max_val.append(max(sside_nums))
        
        elif next_idx == 3:
            side_index = [0, 2, 4, 5]
            up_index = 1

            sside_nums = []
            for iidx in side_index:
                sside_nums.append(dice_arr[i + 1][iidx])

            max_val.append(max(sside_nums))

        elif next_idx == 4:
            side_index = [0, 1, 3, 5]
            up_index = 2

            sside_nums = []
            for iidx in side_index:
                sside_nums.append(dice_arr[i + 1][iidx])

            max_val.append(max(sside_nums))

        else:
            side_index = [1, 2, 3, 4]
            up_index = 0

            sside_nums = []
            for iidx in side_index:
                sside_nums.append(dice_arr[i + 1][iidx])

            max_val.append(max(sside_nums))
    
    if sum(max_val) >= ans:
        ans = sum(max_val)
        max_val.clear()
    else:
        max_val.clear()

print(ans)


# N = int(input())
# dice_arr = [list(map(int, input().split())) for _ in range(N)]

# max_val = 0
# for d in range(N):              # 다이스 개수만큼
#     for i in range(6):              # 주사위 6면
#         facedown_idx = i
#         side_nums = []

#         if facedown_idx == 0:
#             faceup_idx = 5
#             side_index = [1, 2, 3, 4]
#         elif facedown_idx == 1:
#             faceup_idx = 3
#             side_index = [0, 2, 4, 5]
#         elif facedown_idx == 2:
#             faceup_idx = 4
#             side_index = [0, 1, 3, 5]
#         elif facedown_idx == 3:
#             faceup_idx = 1
#             side_index = [0, 2, 4, 5]
#         elif facedown_idx == 4:
#             faceup_idx = 2
#             side_index = [0, 1, 3, 5]
#         elif facedown_idx == 5:
#             faceup_idx = 0
#             side_index = [1, 2, 3, 4]

#         for k in side_index:      # 옆면 중 가장 큰 수를 더해주기
#             side_nums.append(dice_arr[i][k])

#         max_val += max(side_nums)
     
#     # 다음 위에 쌓는 주사위
#     for p in range(N - 1):  # 첫 주사위를 뺀 나머지 주사위개수
#             # 이전 hidden 값의 idx와 마주보는 값 (위로 올라가는 값)
#         next_facedown_idx = dice_arr[p + 1].index(dice_arr[p][faceup_idx])

#         if next_facedown_idx == 0:
#             side_nums.a
#         elif next_idx == 1:
#                 hidden_nums.append(next_dice[i][3])
#         elif next_idx == 2:
#                 hidden_nums.append(next_dice[i][4])
#         elif next_idx == 3:
#                 hidden_nums.append(next_dice[i][1])
#         elif next_idx == 4:
#                 hidden_nums.append(next_dice[i][2])
#         else:
#                 hidden_nums.append(next_dice[i][0])

#         ans = hidden_nums.count(6)
#         for k in range(N - 1):
#             if hidden_nums[k:k + 1] == [6, 5]:
#                 ans += 1
#             elif hidden_nums[k:k + 1] == [5, 6]:
#                 ans += 1

#         cnt_six.append(ans)

#     result = 6 * N - min(cnt_six) - 1
# print(result)