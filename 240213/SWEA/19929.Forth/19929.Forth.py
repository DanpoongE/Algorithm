def Forth(arr):
    stack = []  # 빈 스택 준비

    for items in arr:
        if items in '*/+-' and len(stack)>=2: # 연산자이고 stack에 숫자가 2개 이상이면 두개 pop
            b = int(stack.pop())
            a = int(stack.pop())

            if items == '+':
                stack.append(a+b)
            elif items == '-':
                stack.append(a-b)
            elif items == '*':
                stack.append(a*b)
            else:
                stack.append(a//b)

        elif items in '*/+-' and len(stack)<2: # 연산자이고 stack에 숫자가 1개 이하면 Error
            return 'error'
            break

        elif items == '.' and len(stack)==1:
            return stack[0]

        else: # 피연산자면 stack에 넣기
            stack.append(items)
    if len(stack) > 1:
        return 'error'





T=int(input())

for tc in range(1, T+1):
    arr = list(input().split())

    print(f'#{tc}', Forth(arr))
