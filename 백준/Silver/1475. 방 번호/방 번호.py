import sys
import math
input = sys.stdin.readline

exam = list(input().strip())
check = {}

for i in range(9) :
    check[i] = 0

for i in exam :
    if i == '6' or i == '9' :
        check[6] += 1
    else :
        check[int(i)] += 1

check[6] = math.ceil(check[6]/2)

print(max(check.values()))