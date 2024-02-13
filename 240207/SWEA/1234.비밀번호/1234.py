T = 10

for tc in range(1, T+1):
    N, numbers = input().split()
    N = int(N)
    numbers = list(numbers)

    temp_numbers = []

    for x in numbers:
        if temp_numbers and temp_numbers[-1] == x:
            temp_numbers.pop()

        else:
            temp_numbers.append(x)

        result = ''.join(temp_numbers)
    print(f'#{tc} {result}')
