# # 테스트케이스 T를 받는다.
#
# T = int(input())
# # 정수 형태로 input을 받는다.
# print(T)
# for t in range(T):   # T번 반복해서 testcase별 입력 받기
#     N = int(input())  # N개의 입력
#     a = list(map(int, input().split()))  # 각각의 요소 string을 int로 변환
#
#     max_val = max(a)
#     min_val = min(a)
#     print(f'#{t+1} {max_val - min_val}')

T = int(input())  # 테스트 케이스의 개수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 빌딩의 개수
    building_list = list(map(int, input().split()))

    result = 0

    for bld in range(N):
        if building_list[bld] != 0:
            nxt_i = [-2, -1, 1, 2]
            max_height = 0

            for i in range(4):
                if max_height < building_list[bld + nxt_i[i]]:
                    max_height = building_list[bld + nxt_i[i]]

                    if building_list[bld] > max_height:
                        result += building_list[bld] - max_height
        else:
            pass

print(f'#{test_case} {result}')