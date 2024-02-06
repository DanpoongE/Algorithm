T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(str, input().split())) for _ in range(N)]

    # 행렬 형태로 만들어야 합니당




    # 행의 숫자 i
    for i in range(N):
        word = arr[i][0]
    
        for j in range(N-M+1):
            new_word = word[j:j+M]
            reversed_word = new_word[::-1]
    
            if new_word == reversed_word:
                print(f'#{tc} {new_word}')
    #
    # # 열
    # for j in range(N):
    #     for i in range(N):
    #         word = arr[i][j]
    #         print(word)
    # # 전치 행렬로 바꾸기
    # # for i in range(N):
    #     # for j in range(N):
    #     #     arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


