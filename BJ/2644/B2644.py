N = int(input())
targets = list(map(int, input().split()))
# targets.sort()
M = int(input())
parent_of = [0] * (N + 1)

for _ in range(M):
    pa, ch = list(map(int, input().split()))
    parent_of[ch] = pa

tar1 = targets[0]
tar2 = targets[1]       # 더 큰 수가 tar2가 된다.
parents1 = []           # tar1의 부모 노드들을 담을 리스트
parents2 = []           # tar2의 부모 노드들을 담을 리스트
ans = 0

while parent_of[tar2] != 0:
    parents2.append(parent_of[tar2])
    if parent_of[tar2] == tar1:     # tar1이 tar2의 부모노드였다면 리스트 길이가 정답
        ans = len(parents2)
        break
    else:                           # tar1이 tar2의 부모노드가 아니라면
        tar2 = parent_of[tar2]

tar2 = targets[1]       # 초기화
if ans != 0:
    print(ans)

else:
    while parent_of[tar1] != 0:
        parents1.append(parent_of[tar1])
        if parent_of[tar1] == tar2:         # tar2가 tar1의 부모노드라면 리스트 길이가 정답
            ans = len(parents1)
            break
        elif parent_of[tar1] in parents2:    # tar1의 부모 노드가 tar2의 부모 노드 중에 있다면
            ans = parents1.index(parent_of[tar1]) + parents2.index(parent_of[tar1]) + 2
            break
        else:
            tar1 = parent_of[tar1]

    if ans != 0:
        print(ans)

    else:
        print(-1)