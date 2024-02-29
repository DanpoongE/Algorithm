def perfect_shuffle():
    a = 0
    b = (len(cards) + 1) // 2

    for turn in range(len(cards)):
        if turn % 2 == 0:       # 짝수면 a
            print(cards[a], end = ' ')
            a += 1

        else:                   # 홀수면 b
            print(cards[b], end = ' ')
            b                                                                                                                                                                                                                                                             += 1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(input().split())

    print(f'#{tc}', end=' ')
    perfect_shuffle()
    print()

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     cards = list(input().split())
#
#     a = 0
#     if N % 2 == 0:
#         b = N // 2
#     else:
#         b = N // 2 + 1
#
#     shuffle = []
#
#     while len(shuffle) != len(cards):
#         if a < N // 2:
#             shuffle.append(cards[a])
#             a += 1
#         if b < N:
#             shuffle.append(cards[b])
#             b += 1
#
#     print(*shuffle)
