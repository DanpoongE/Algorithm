from collections import deque

# q = deque()
# q.append(1)
# q.append(2)
# print(q.popleft())

dq = deque()
for i in range(10000):
    dq.append(i)
print('append')
while dq:
    dq.popleft()
print('end')