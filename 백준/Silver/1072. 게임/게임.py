import sys

import math

input = sys.stdin.readline

x, y = list(map(int, input().split()))

z = (100*y)//x

num = 0

ans = -1

if z < 99 :

    ans = ((z+1)*x-100*y+99-z-1)//(99-z)

print(ans)    