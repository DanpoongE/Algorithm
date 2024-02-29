T = int(input())

for tc in range(1, T + 1):
    nums, move = list(input().split())
    board = list(map(int, list(nums)))      # 주어진 숫자들
    M = int(move)                           # 이동 횟수 M


#     max_val = list(reversed(sorted(board)))       # 해당 board 숫자로 만들 수 있는 최대 수
#
#     change_cnt = 0
#
#     # 시작하기 전에 숫자 2개로만 이루어진 board는 특수하므로 따로 구현
#     if len(board) == 2:
#         if move % 2 == 0:               # 짝수번 교환이라면
#             print(f'#{tc}', end=' ')
#             print(*board, sep='')       # 무조건 원래 숫자
#
#         else:                           # 홀수번 교환이라면
#             board[0], board[1] = board[1], board[0]
#             print(f'#{tc}', end=' ')
#             print(*board, sep='')       # 앞뒤 교환한 숫자
#
#     else:                               # 숫자가 3개 이상이라면
#        for change in range(M):               # M번 자리 바꿀 건데
#            if board == max_val:         # 현재 보드 숫자가 최댓값과 동일하다면
#                if M % 2 == 0:  # 짝수번 교환이라면
#                    print(f'#{tc}', end=' ')
#                    print(*board, sep='')  # 무조건 원래 숫자
#                    break
#                else:  # 홀수번 교환이라면
#                    board[0], board[1] = board[1], board[0]
#                    print(f'#{tc}', end=' ')
#                    print(*board, sep='')  # 앞뒤 교환한 숫자
#                    break
#
#            else:                        # 현재 보드 숫자가 최댓값과 같지 않다면 자릿수를 볼건데
#                 if board[change] != max_val[change]:    # 최댓값과 현재값의 M번째 자리수가 다르면 교환
#                     # 제일 뒷자리에 있는 최댓값 찾으려고 현재 board 한번 뒤집어줍니다.
#                     rev_board = list(reversed(board))
#                     max_idx_in_rev = rev_board.index(max_val[change])
#                     max_idx = -(max_idx_in_rev + 1)
#                     board[change], board[max_idx] = board[max_idx], board[change]
#                     change_cnt += 1
#
#                     if change_cnt == M: # 마지막 교환이면
#                         print(f'#{tc}', end=' ')
#                         print(*board, sep='')
#
#                 else:                                   # 최댓값과 현재값의 M번째 자리수가 같다면
#                     while board[change] == max_val[change]:
#                         change += 1                         # 그 다음 자리 볼거야
#                         # 제일 뒷자리에 있는 최댓값 찾으려고 현재 board 한번 뒤집어줍니다.
#                         rev_board = list(reversed(board))
#                         max_idx_in_rev = rev_board.index(max_val[change])
#                         max_idx = -(max_idx_in_rev + 1)
#                         board[change], board[max_idx] = board[max_idx], board[change]
#                         change_cnt += 1
#
#                         if change_cnt == M:  # 마지막 교환이면
#                             print(f'#{tc}', end=' ')
#                             print(*board, sep='')
#                             break