for tc in range(4):
    squares = list(map(int, input().split()))
    flag = 0

    # 왼쪽 아래 꼭짓점 좌표가 빠른 게 1번 사각형
    if squares[0] > squares[4]:
        squares[0:4], squares[4:8] = squares[4:8], squares[0:4]

    # b가 출력되는 경우
    if flag == 0 and squares[2] == squares[4]:       # 두 직사각형이 좌우로 겹치고
        if squares[1] <= squares[5] < squares[3] or squares[1] < squares[7] <= squares[3]:   # y좌표도 겹칠 경우
            print('b')
            flag = 1

    if flag == 0 and squares[3] == squares[5] or squares[1] == squares[7]:      # 두 직사각형이 상하로 겹치고
        if squares[0] <= squares[4] < squares[2] or squares[0] < squares[6] <= squares[2]:
            print('b')
            flag = 1

    # c가 출력되는 경우
    if flag == 0 and squares[2] == squares[4]:
        if squares[3] == squares[5] or squares[1] == squares[7]:
            print('c')
            flag = 1

    # d가 출력되는 경우
    if flag == 0 and (squares[2] < squares[4]):       # x좌표 저멀리
        print('d')
        flag = 1

    if flag == 0 and (squares[3] < squares[5]) or (squares[1] > squares[7]):       # y좌표 저멀리
        print('d')
        flag = 1

    # if flag == 0 and squares[2] == squares[4]:      # x좌표 딱 경계에
    #     if squares[3] < squares[5] or squares[1] > squares[7]:
    #         print('d')
    #         flag = 1
    #
    # if flag == 0 and squares[3] == squares[5]:           # y좌표 딱 경계에, 하상
    #     if squares[2] < squares[4]:
    #         print('d')
    #         flag = 1
    #
    # if flag == 0 and squares[1] == squares[7]:           # y좌표 딱 경계에, 상하
    #     if squares[2] < squares[4]:
    #         print('d')
    #         flag = 1

    # 나머지는 a 출력
    if flag == 0:
        print('a')


    # a가 출력되는 경우
    # board = [[0] * 1000 for _ in range(1000)]
    # # 1번 사각형부터 채우기
    # for i in range(squares[0], squares[2] + 1):
    #     for j in range(squares[1], squares[3] + 1):
    #         board[i][j] += 1
    # # 2번 사각형 채우기
    # for ii in range(squares[4], squares[6] + 1):
    #     for jj in range(squares[5], squares[7] + 1):
    #         if board[ii][jj] == 1:
    #             print('a')
    #             flag = 1
    #             break
    #     if flag == 1:
    #         break


    # elif squares[0] <= squares[4] < squares[2]:     # x좌표가 겹치고
    #     if squares[3] == squares[5] or squares[1] == squares[7]:                # 1번 끝, 3번 시작 y좌표가 같을 경우
    #         print('b')
    #
    # elif squares[2] == squares[4]:                  # x좌표 동일하고
    #     if squares[5]< squares[3] <= squares[7] or squares[1] < squares[7] <= squares[3]:
    #         print('b')

