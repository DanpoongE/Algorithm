# 버정 5000개. 번호붙어있음
# 버스 노선은 N개.
# i번째는 Ai<= <=Bi인 모든 정류장 다니는 버스.
# p개의 버스 정류장. 각 정류장에 몇 개의 버스 노선이 다니는가.

T = int(input())

for tc in range(T):
    route = int(input())
    bus = []
    for where in range(route):
        start, end = map(int, input().split())

        # str사이의 공백은 split할 때 사라짐.
        # 노선 시작 정류장, 끝 정류장 찾음 1,3 / 2,5
        # 이 범위에 있는 숫자의 index-1 의 list값을 하나씩 증가시키고 싶은데...
    print(bus)
    # P = int(input())
    # count_list = [0]*P

        # for i in range(start, end+1):
        #     if i >= start:
        #         if i <= end:
        #             count_list[i-1] += 1

# 시작, 끝 범위 내의 정류장 count 증가.
    # print(count_list)


