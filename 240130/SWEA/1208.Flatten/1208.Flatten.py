# 평탄화 문제

# 덤프 횟수만큼 반복
# 제일 높이 있는 곳의 상자 -> 제일 낮은 곳으로. height 재야겠는데?

T = 10 # 테스트 케이스는 10개

for test_case in range(1, T+1):
    D = int(input()) # 덤프 횟수
    box_list = list(map(int, input().split()))
    box_list.sort() # 상자 높이 오름차순으로 정렬.
    # 덤프 횟수만큼 빼고 더할거야.

    for height in range(D): # 덤프 횟수만큼
        box_list[-1] -= 1
        box_list[0] += 1
        box_list.sort()

        if max(box_list) - min(box_list) <= 0:
            break

    result = max(box_list) - min(box_list)
    print(f'#{test_case} {result}')


