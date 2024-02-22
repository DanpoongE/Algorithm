'''
5
0 1 1 3 2
'''

N = int(input())        # 학생수
move = list(map(int, input().split()))  # 이동횟수 리스트

line_up = [0] * N
for i in range(N): # 처음 줄을 선 순서
    line_up[i] = i+1

# 인덱스 번호에서 이동 횟수 만큼 빼면 새로운 인덱스가 나타난다.
for nums in line_up:
    old_idx = line_up.index(nums)
    new_idx = old_idx - move[old_idx]

    # 새 인덱스 <= < 기존 인덱스 사이에 있었던 숫자들은 +1씩 뒤로 이동.
    line_up[new_idx+1:old_idx+1] = line_up[new_idx:old_idx]

    # 숫자는 새로운 인덱스 위치로 이동
    line_up[new_idx] = nums

print(*line_up)