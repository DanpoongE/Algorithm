import sys
sys.stdin = open('B2304.txt')

N = int(input())
garrage = [0] * 1002
end = 0
for _ in range(N):
    L, H = list(map(int, input().split()))
    garrage[L] = H
    
    if end <= L:
        end = L + 1

garrage = garrage[0 : end]
max_val = max(garrage)
max_idx = garrage.index(max_val)

forward_garrage = garrage[0 : max_idx + 1]
for c in range(max_idx + 1):
    if c + 1 < max_idx + 1:
        if forward_garrage[c] >= forward_garrage[c + 1]:
            forward_garrage[c + 1] = forward_garrage[c]

backward_garrage = garrage[max_idx + 1 : end]
backward_garrage.reverse()
for cc in range(len(backward_garrage)):
    if cc + 1 < len(backward_garrage):
        if backward_garrage[cc + 1] <= backward_garrage[cc]:
            backward_garrage[cc + 1] = backward_garrage[cc]

backward_garrage.reverse()

print(sum(forward_garrage) + sum(backward_garrage))