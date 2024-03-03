import sys
sys.stdin = open('B1244.txt')

N = int(input())
switch = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    gender, number = list(map(int, input().split()))

    if gender == 1:     # 남학생이면
        i = 1
        while number * i <= N:
            if switch[number * i - 1] == 0:    # 스위치가 꺼져 있으면
                switch[number * i - 1] = 1
                i += 1

            else:   # 스위치가 켜져 있으면
                switch[number * i - 1] = 0 
                i += 1
    
    else:               # 여학생이면
        center_idx = number - 1
        j = 0
        left_idx = center_idx - 1
        right_idx = center_idx + 1
        
        while left_idx >= 0 and right_idx < N and switch[left_idx] == switch[right_idx]:
            j += 1
            left_idx -= 1
            right_idx += 1
        
        if j == 0:              # center_idx 값만 바뀌면 됨
            if switch[center_idx] == 0:
                switch[center_idx] = 1
            else:
                switch[center_idx] = 0
        else:
            if switch[center_idx] == 0:
                switch[center_idx] = 1
            else:
                switch[center_idx] = 0
            for k in range(1, j + 1):
                if switch[center_idx + k] == 0:
                    switch[center_idx + k] = 1
                else:
                    switch[center_idx + k] = 0
                
                if switch[center_idx - k] == 0:
                    switch[center_idx - k] = 1
                else:
                    switch[center_idx - k] = 0

for idx in range(0, N, 20):
    print(*switch[idx:idx + 20])