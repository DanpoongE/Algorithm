import sys
sys.stdin = open('B10158.txt')

w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
t = int(input())

# x좌표
if (t - (w - p)) // w % 2 == 1:   # 몫이 홀수면
    x = (t - (w - p)) % w
elif (t - (w - p)) // w % 2 == 0:   # 짝수면
    x = w - (t - (w - p)) % w

# y좌표
if (t - (h - q)) // h % 2 == 1:
    y = (t - (h - q)) % h
elif (t - (h - q)) // h % 2 == 0:
    y = h - (t - (h - q)) % h

print(x, y)


# direction1 = 'right'
# direction2 = 'up'

# for _ in range(t):
#     if p == w:          # 오른쪽 경계에 다다르면
#         direction1 = 'left'
#     elif p == 0:        # 왼쪽 경계에 다다르면
#         direction1 = 'right'
    
#     if q == h:          # 위쪽 경계에 다다르면
#         direction2 = 'down'
#     elif q == 0:        # 아래쪽 경계에 다다르면
#         direction2 = 'up'
    
#     if direction1 == 'right' and direction2 == 'up':
#         p += 1
#         q += 1
#     elif direction1 == 'right' and direction2 == 'down':
#         p += 1
#         q -= 1
#     elif direction1 == 'left' and direction2 == 'up':
#         p -= 1
#         q += 1
#     elif direction1 == 'left' and direction2 == 'down':
#         p -= 1
#         q -= 1
    
# print(p, q)