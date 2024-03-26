from itertools import combinations

def avail_honey(startpoint):
    max_honey = 0
    avail = []
    for r in range(N):      # 행마다 탐색
        for c in range(startpoint, N, M):    # 열은 첫 시작점부터 N-1까지 M 만큼의 간격으로
            select = arr[r][c:c + M]
            avail.append(max_combi(select))

        avail.sort()
    max_honey += avail.pop()
    max_honey += avail.pop()
    return max_honey

def max_combi(lst):
    max_com = 0
    if sum(lst) <= C: # 선택한 벌통의 합이 최대양보다 작거나 같은 경우
        for honey in lst:
            max_com = max_com + honey**2
    else: # 선택한 벌통의 합이 채취가능양을 초과하는 경우
        for l in range(M - 1, 0, -1):  # 1부터 M까지
            for combin in combinations(lst, l):
                total = 0
                if sum(combin) <= C:  # 채취가능양을 초과하지 않는 조합일 때
                    for combi in combin:
                       total = total + combi**2
                    if total > max_com: # 벌통의 합이 해당 조합에서 구한 최대값(max_com)보다 크면
                        max_com = total

    return max_com


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for startpoint in range(0, M):      # 인덱스 [0, 2, 4], [1, 3, 5] 끼리 확인
        if ans < avail_honey(startpoint):
            ans = avail_honey(startpoint)
        # max_honey += avail_honey(startpoint).pop()
        # max_honey += avail_honey(startpoint).pop()

    print(f'#{tc}', ans)
