T = int(input())
code_dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}


for C in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(str, input())) for _ in range(N)]
    # 각 행마다 거꾸로 뒤집어
    for i in range(N):
        arr[i].reverse()
    # 행렬을 순회하면서 처음 1이 나오는 위치를 si, sj라고 할건데 그거 찾아
    found_code = 0
    si = 0
    sj = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                si = i
                sj = j
                found_code = 1
                break
        if found_code:
            break
    # 그 부분부터 len56 이 되도록 slicing할거야.
    reversed_code = arr[si][sj:sj+56]            # 이건 reverse 된 거니까
    reversed_code.reverse()                      # 한번 더 뒤집고
    code = ''.join(reversed_code)                # 이래야 진짜 코드!

    # 진짜 코드를 7개씩 잘라서 숫자로 바꿀겁니당
    decode = []
    for k in range(8):
        slice_code = code[k * 7 : k * 7 + 7]
        decode.append(code_dict[slice_code])

    # decode 리스트에 담긴 숫자들이 올바른 암호코드인지 확인
    #홀수 자리의 합
    odd_sum = decode[0] + decode[2] + decode[4] + decode[6]
    # 짝수 자리의 합
    even_sum = decode[1] + decode[3] + decode[5] + decode[7]

    check = odd_sum * 3 + even_sum

    if check % 10 == 0:
        print(f'#{C} {sum(decode)}')

    else:
        print(f'#{C} {0}')