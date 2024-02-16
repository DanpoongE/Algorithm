# q = []
# q.append(1)
# q.append(2)
# q.append(3)
#
# print(q.pop(0)) #1 (pop은 뒤에서부터 보기 때문에 시간복잡도상 매우 좋지 않다는 거! 알쥐알쥐)
#
# # 다 꺼내려면 while queue:


q = [0] * 10
front = rear = -1

rear += 1       # enqueue(10)
q[rear] = 10

rear += 1       # enqueue(20)
q[rear] = 20

rear += 1       # enqueue(30)
q[rear] = 30

while front!=rear: # 큐가 비어있지 않으면
    front += 1
    print(q[front]) # 앞에서부터 꺼내려면 front 필수임임