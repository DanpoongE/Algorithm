# li = ['s', 'o', 'f']
# print(''.join(li))
#
# #'구분자'.join(리스트): join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수입니다.



# 팩토리얼 함수 만들기
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)


print(f(6))
