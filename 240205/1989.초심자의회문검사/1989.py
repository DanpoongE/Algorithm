T = int(input())

for tc in range(1, T+1):
    word = str(input())
    reversed_word = word[::-1]

    result = 0

    if word == reversed_word:
        result = 1

    print(f'#{tc} {result}')