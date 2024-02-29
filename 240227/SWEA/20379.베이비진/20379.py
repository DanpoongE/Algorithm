T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1_list = []
    player2_list = []
    result = 0

    for i in range(12):
        if i % 2 == 0:  # 홀수번째 카드(인덱스는 짝수)면
            player1_list.append(cards[i])

        else:           # 짝수번째 카드면
            player2_list.append(cards[i])

        # 카드 3개 이상부터 베이비진 확인
        if len(player1_list) >= 3:
            player1_list.sort()

            for k in range(4):
                if (k + 2) < len(player1_list) and player1_list[k] == player1_list[k + 1] == player1_list[k + 2]:  # triplet
                    result += 1
                    break

            if result == 0: # run
                cnt = 0
                for nums in range(10):
                    if nums in player1_list:
                        cnt += 1
                        if cnt == 3:
                            result += 1
                            break

                    else:
                        cnt = 0

        if len(player2_list) >= 3:
            player2_list.sort()

            for k in range(4):
                if (k + 2) < len(player2_list) and player2_list[k] == player2_list[k + 1] == player2_list[k + 2]:  # triplet
                    result += 2
                    break

            if result == 0:  # run
                cnt = 0
                for nums in range(10):
                    if nums in player2_list:
                        cnt += 1
                        if cnt == 3:
                            result += 2
                            break

                    else:
                        cnt = 0

        if result != 0:     # 플레이어 둘 중 한명이라도 베이비진 완성시 끝끝
            break
    print(f'#{tc}', result)