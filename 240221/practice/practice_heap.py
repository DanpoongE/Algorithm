# 최대힙
def enqueue(n):
    # 마지막 노드 추가(완전이진트리 유지)
    global last
    last += 1           # 마지막 노드 추가(완전이진트리 유지)
    heap[last] = n      # 마지막 노드에 데이터 삽입
    c = last            # 부모 > 자식
    p = c//2            # 부모 노드 번호 (이진트리에서)

    while p >= 1 and heap[p] < heap[c]:         # 부모가 존재하고(그냥 p도 오케이이), 부모 값이 더 작다면
        heap[p], heap[c] = heap[c], heap[p]     # 교환
        c = p
        p = c//2
        print(heap)



# 삭제 코드
def dequeue():
    global last
    tmp = heap[last]       # 루트의 키 값 보관
    heap[1] = heap[last]
    last -= 1
    p = 1                   # 새로 옮긴 루트
    c = p*2

    while c <= last:        # 자식이 하나라도 있다면
        if c+1 <= last and heap[c] < heap[c+1]:     # 오른쪽 자식이 있고 만약 더 크면
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c                                   # 새로운 자식으로 해서
            c = p*2
        else:
            break

    return tmp

N = 10                  # 필요한 노드 수
heap = [0] * (N+1)      # 최대힙
last = 0                # 힙의 마지막 노드 번호 (0부터 시작)

enqueue(2)
enqueue(5)
enqueue(3)
enqueue(6)
enqueue(4)
while last > 0:
    print(dequeue())