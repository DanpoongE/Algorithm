T = 10


for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    stack = []
    # top = -1    # 이건 또 언제 필요한건지 모르겠어
    result = [] # 후위표기식 담을거
    # print(arr)

# 후위표기식으로 바꾸기
    ip = {'+' : 1, '*' : 2}

    for i in arr:
        if i not in '+*':   # 숫자라면 result에 출력
            result.append(i)
        elif stack and (ip[i] > ip[stack[-1]]): # 연산자이고 스택에 있던 것보다 우선순위가 높으면
            # 즉, stack[-1]=+이고 push하려는게 *이면
            stack.append(i)
        elif stack and (ip[i] <= ip[stack[-1]]): # 연산자이고 스택에 있던 것보다 우선순위가 높지 않으면
            while stack and (ip[i] <= ip[stack[-1]]): # 우선순위가 더 낮은 게 스택 가장 위에 오거나, 스택이 빌 때까지
                result.append(stack.pop())
            stack.append(i)
        else: # 첫 연산자라면
            stack.append(i)

    while stack:
        result.append(stack.pop()) # 마지막에 stack에 남는 연산자 붙여주기
    # print(result)


# 이제 계산하기
    for j in result:
        if j not in '+*':   # 숫자라면 stack에 push
            stack.append(j)
        else:   # 연산자라면 2개 pop
            b = int(stack.pop())
            a = int(stack.pop())

            if j == '+':
                stack.append(a+b)
            else: # 곱셈이라면
                stack.append(a*b)

    print(f'#{tc}', *stack)