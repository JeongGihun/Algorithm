import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
ans = 1
# a를 b번 곱해서 c로 나눈 수 구하기
# 분할 정복
while b != 0 :
    if b % 2 == 0 :
        b //= 2
        a = pow(a, 2) % c
    else :
        b -= 1
        ans = ans * a % c
print(ans)