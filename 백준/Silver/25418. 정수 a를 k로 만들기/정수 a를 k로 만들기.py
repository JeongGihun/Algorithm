import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
cnt = 0
while True :
    if n == m :
        break
    if m % 2 == 0 and m // 2 >= n:
        m //= 2
    else :
        m -= 1
    cnt += 1
print(cnt)