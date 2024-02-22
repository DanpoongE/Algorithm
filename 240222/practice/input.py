import sys
sys.stdin = open('input.txt', 'r')
# 콘솔로 입력받지 않아도 텍스트 파일로부터 값을 가져올 수 있다.

sys.stdout = open('output.txt', 'w')
# output이라는 txt 파일에 결과값이 출력된다.

a, b = input().split()
a = int(a)
b = int(b)
print(a+3, b+3)