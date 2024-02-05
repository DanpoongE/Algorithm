T = int(input())

for tc in range(1, T+1):
    N = int(input())                     # 카드 장 수
    arr = list(map(int, input()))
                                         # 특정 카드의 장 수를 세어볼까욥?
    cnt = [0]*10                         # ai가 9까지잖아욥
    for i in arr:
        cnt[i] += 1
    # print(cnt)

    max_cnt = max(cnt)                   # 제일 큰 '장 수' 찾아욥

    # count 해서 큰 수가 여러장인지 봅시다.
    if cnt.count(max_cnt) == 1:     # max값이 하나라면 그친구 인덱스와 max_cnt 출력할게욥
        print(f'#{tc} {cnt.index(max_cnt)} {max_cnt}')

    else:                           # 아니라면 제일 마지막 max값(max_cnt)의 index를 출력!
        for j in range(9, -1, -1):  # 마지막 인덱스 찾으려고 뒤에서부터 돌릴게요~
            if cnt[j] == max_cnt:
                print(f'#{tc} {j} {max_cnt}')
                break