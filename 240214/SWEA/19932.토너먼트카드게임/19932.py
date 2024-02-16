T = int(input())

def rsp(index1, index2):
    # index1 < index2 -> 비겼을 때 인덱스가 작은 쪽이 이긴다
    card1 = cards[index1]
    card2 = cards[index2]
    # 1: 가위, 2: 바위, 3: 보
    if card1 == '1' and card2 == '2':
        return index2
    if card1 == '2' and card2 == '3':
        return index2
    if card1 == '3' and card2 == '1':
        return index2
    return index1 # 비겨도 얘가 이기기 때문

def divide(start, end):
    if start == end:
        return start
    group1 = divide(start, (start+end)//2)
    group2 = divide((start+end)//2+1, end)
    return rsp(group1, group2)

for tc in range(1, T+1):
    N = int(input())        # 인원수
    cards = input().split()
    print(f'#{tc}', end=' ')

    answer = divide(0, len(cards) - 1)
    print(answer+1) #answer는 인덱스니까 +1해준 것