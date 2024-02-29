'''
{A, B, C, D, E} 중 최소 2명 이상의 친구를 선정하여
카페에 가는 경우의 수
'''

# 하드코딩
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        # 1비트 1인지 확인
        if tar & 0x1:           # tar은 또 언제 2진수로 바뀐단말임?
            cnt += 1

        # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return cnt

result = 0

for tar in range(1 << n):
    if get_count(tar) >= 2:     # bit가 2개이상 1이라면 -> 2명 이상이라면
        result += 1

print(result)