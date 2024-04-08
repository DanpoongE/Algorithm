from collections import deque

def destination():
    to_go.append(house)  # 시작점과
    visited.add(house)  # visited 기록해주고 시작

    while to_go:
        start = to_go.popleft()
        if abs(start[0] - fiesta[0]) + abs(start[1] - fiesta[1]) <= 1000: # 출발지에서 축제위치에 도착할 수 있다면
            print('happy')
            return

        for store in stores:
            if abs(store[0] - start[0]) + abs(store[1] - start[1]) <= 1000: # 갈 수 있는 영역에 있고
                if store not in visited:       # 간 적 없는 곳이면
                    to_go.append(store)
                    visited.add(store)

    print('sad')
    return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())        # 편의점 개수
    house= tuple(map(int, input().split())) # 집 좌표
    stores = []             # 편의점 좌표 저장할 리스트
    for _ in range(N):                      # 편의점 개수만큼 좌표 찾아서 list에 넣기
        node = tuple(map(int, input().split()))
        stores.append(node)
    fiesta = tuple(map(int, input().split()))   # 축제 장소 좌표
    final_position = house # 마지막으로 선 위치. 집에서 시작하므로 집 위치를 처음 넣어준다.

    to_go = deque()
    visited = set()         # 방문한 편의점을 기록해주기 위한 set

    destination()  # 다음 도착지 구하는 함수
