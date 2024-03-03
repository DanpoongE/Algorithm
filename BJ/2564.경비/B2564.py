import sys
sys.stdin = open('B2564.input.txt')

w, h = list(map(int, input().split()))
N = int(input())
stores = [[0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    store_info = list(map(int, input().split()))
    stores[i] = store_info

guard_direction, guard_loca = list(map(int, input().split()))

short_distance = 0
for s in range(1, N + 1):
    store_direction = stores[s][0]
    store_loca = stores[s][1]

    if store_direction == guard_direction:  # 동근이와 상점이 같은 라인일 때
        short_distance += abs(store_loca - guard_loca)  # 위치 차이값이 최솟값
    
    else:       # 동근이와 상점이 다른 라인에 위치할 때
        if guard_direction == 1: # 동근이는 북쪽에 있고
            if store_direction == 3: # 가게는 서쪽에 있을 때
                short_distance += store_loca + guard_loca
            elif store_direction == 4: # 가게는 동쪽에 있을 때
                short_distance += store_loca + (w - guard_loca)
            else: # 가게는 남쪽에 있을 때
                left_distance = store_loca + h + guard_loca
                right_distance = (w - store_loca) + h + (w - guard_loca)
                if left_distance < right_distance:
                    short_distance += left_distance
                else:
                    short_distance += right_distance

        elif guard_direction == 2: # 동근이는 남쪽에 있고
            if store_direction == 1: # 가게는 북쪽에
                left_distance = guard_loca + h + store_loca
                right_distance = (w - guard_loca) + h + (w - store_loca)
                if left_distance < right_distance:
                    short_distance += left_distance
                else:
                    short_distance += right_distance
            elif store_direction == 3: # 가게는 서쪽에
                short_distance += guard_loca + (h - store_loca)
            else: # 가게는 동쪽에
                short_distance += (w - guard_loca) + (h - store_loca)
        
        elif guard_direction == 3: # 동근이는 서쪽에
            if store_direction == 1: # 가게는 북쪽에
                short_distance += guard_loca + store_loca
            elif store_direction == 2: # 가게는 남쪽에
                short_distance += (h - guard_loca) + store_loca
            else: # 가게는 동쪽에
                up_distance = guard_loca + w + store_loca
                down_distance = (h - guard_loca) + w + (h - store_loca)
                if up_distance < down_distance:
                    short_distance += up_distance
                else:
                    short_distance += down_distance
        
        elif guard_direction == 4: # 동근이는 동쪽에 (조건을 잘 보이게 하려고 else 안 씀)
            if store_direction == 1: # 가게는 북쪽에
                short_distance += guard_loca + (w - store_loca)
            elif store_direction == 2: # 가게는 남쪽에
                short_distance += (h - guard_loca) + (w - store_loca)
            else: # 가게는 서쪽에
                up_distance = guard_loca + w + store_loca
                down_distance = (h - guard_loca) + w + (h - store_loca)
                if up_distance < down_distance:
                    short_distance += up_distance
                else:
                    short_distance += down_distance

print(short_distance)