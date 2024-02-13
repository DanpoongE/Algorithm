def fibo(n):
    global cnt
    cnt +=1
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

cnt = 0
print(fibo(7), cnt)


def fibo_memo(n):
    if



counts = 0
n = 7

memo = [0]*(n+1)
memo[0] = 0
memo[1] = 1