# 계산식을 후위표기식으로 바꾸고
T = 10
for tc in range(1, T+1):
    N = int(input())    # 문자열 계산식의 길이
    fx = input()        # 수식
    new_fx = ''

    stack = []          # 빈 스텍
    # top = -1
    for i in fx:
        if i in '*/+-' and stack: # 토큰이 연산자이고 stack이 비어있지 않다면
            # 이미 stack에 들어있던 연산자 (기존 +) pop
            new_fx += stack.pop()
            stack.append(i)

        elif i in '*/+-': # 토큰이 연산자이고 stack이 비어있다면 push
            stack.append(i)
        else: # 토큰이 피연산자라면 토큰 출력
            new_fx += i
    new_fx += stack.pop() # 남아있는 연산자 다 꺼내기(그래봤자 +하나)
    # print(new_fx)

    # 해당 후위표기식을 계산할 수 있는 프로그램 만들기
    for j in new_fx:
        if j not in '*/+-': # 토큰이 피연산자이면 스택에 push
            # 어차피 stack 비어있을 거니까 재활용할게욥
            stack.append(j)
        else:   # 토큰이 연산자이면 필요한 만큼의 피연산자를 스택에서 pop하여 연산

            b = int(stack.pop()) # int로 바꿔줘야 하나?
            a = int(stack.pop()) # 피연산자는 str일 텐데, 계산이 가능한가?

            # 연산 결과를 다시 스택에 push
            stack.append(a+b)

    print(f'#{tc}', *stack)