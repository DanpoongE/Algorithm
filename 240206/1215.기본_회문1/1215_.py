T = 10

for tc in range(1, T+1):
    M = int(input())
    arr = [list(input()) for _ in range(8)]

    # print(arr)

    # 행 확인
    row_count = 0
    for i in range(8):              # 행 돌림
        for j in range(8-M+1):      # 열 돌릴건데 회문 길이 넘지 않게
            new_list = []           # 빈 리스트 하나 만들고
            for z in range(M):
                new_list.append(arr[i][j+z])    # 0번째 인덱스부터 회문 길이만큼 넣어

            rev_list = list(reversed(new_list)) # 그렇게 만들어진 리스트를 뒤집고
            if new_list == rev_list:            # 그게 원래 리스트와 동일하면 회문
                row_count += 1                  # count 하나 올리기



    # 열 확인
    col_count = 0
    for i in range(8):              # 행 돌림
        for j in range(8-M+1):      # 열 돌릴건데 회문 길이 넘지 않게
            new_list = []           # 빈 리스트 하나 만들고
            for z in range(M):
                new_list.append(arr[j+z][i])    # 0번째 인덱스부터 회문 길이만큼 넣어

            rev_list = list(reversed(new_list)) # 그렇게 만들어진 리스트를 뒤집고
            if new_list == rev_list:            # 그게 원래 리스트와 동일하면 회문
                col_count += 1                  # count 하나 올리기

    print(f'#{tc} {row_count+col_count}')

