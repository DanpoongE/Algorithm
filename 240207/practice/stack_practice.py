def push(n):
    global top
    top += 1            # 먼저 top 하나 올리고
    if top == size:
        print("overflow!")
    else:
        stack[top] = n  # 그 다음 숫자를 넣는다.

top = -1
size = 10           # size는 casebycase로 달라지니까 함수 영역에 놓지 않는 것
stack = [0]*size # 최대 10개 push

top += 1
stack[top] = 10

top +=1
stack[top] = 20

push(30)


while top>=0:
    top -= 1
    print(stack[top+1])     # append와 pop이 속도가 느려지는 순간이 온대. 그때 이거 쓰기