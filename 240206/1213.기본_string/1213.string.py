T = 10

for _ in range(1, T+1):
    tc = int(input())

    #문자열 list로 받자
    txt = list(input())
    #영어문장도 list로 받자
    sentence = list(input())

    count = 0                   # count 초기화해주고
    N = len(txt)
    M = len(sentence)

    for i in range(M-N+1):      # sentence 인덱스 M-N부분까지 훑어서
        if txt == sentence[i:i+N]:
            count += 1

    print(f'#{tc} {count}')


# for _ in range(1, T+1):
#     tc = input()
#     txt = input()
#     sentence = input()
#
#     print(f'#{tc} {sentence.count(txt)}')