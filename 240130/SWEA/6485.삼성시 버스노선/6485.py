# 버정 5000개. 번호붙어있음
# 버스 노선은 N개.
# i번째는 Ai<= <=Bi인 모든 정류장 다니는 버스.
# p개의 버스 정류장. 각 정류장에 몇 개의 버스 노선이 다니는가.
# C1, C2, C3..가 차례대로 1번, 2번, 3번 버정이라는 보장이 없으므로 COUNTS[Cj]로 읽도록 하자

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0]*5001           # 1-5000번 노선을 index 0-4999로 하기 귀찮으므로 index하나 늘리고, 0번은 버리기
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1): # 1<=A<=B<=5000 늘 출발지정류장 번호가 도착점보다 작으므로 가능
            counts[j] += 1
    P = int(input())
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end= ' ')

    for i in busstop: # 출력할 정류장 번호
        print(counts[i], end= ' ')
    print()
        # str사이의 공백은 split할 때 사라짐.
        # 노선 시작 정류장, 끝 정류장 찾음 1,3 / 2,5
        # 이 범위에 있는 숫자의 index-1 의 list값을 하나씩 증가시키고 싶은데...

    # P = int(input())
    # count_list = [0]*P

        # for i in range(start, end+1):
        #     if i >= start:
        #         if i <= end:
        #             count_list[i-1] += 1

# 시작, 끝 범위 내의 정류장 count 증가.
    # print(count_list)


