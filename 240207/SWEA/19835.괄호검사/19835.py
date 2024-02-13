T = int(input())

for tc in range(1, T+1):
    str = input()

    # 소괄호 중괄호를 나누어서 본다! 이러면 안된다! ({)} 이런건 잘못된 괄호라고 판단되어야 한다!
    stack=[]

    for c in str:
        if c == '(':
            stack.append('(')
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif len(stack) > 0 and stack[-1] == '{':
                break
            else:
                stack.append(')')
        elif c == '{':
            stack.append('{')
        elif c == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif len(stack) > 0 and stack[-1] == '(':
                break
            else:
                stack.append('}')

    if len(stack) > 0:
        print(f'#{tc} {0}')

    else:
        print(f'#{tc} {1}')