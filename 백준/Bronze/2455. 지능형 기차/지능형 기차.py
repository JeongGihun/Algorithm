import sys

check = [0]

for _ in range(4) :
    i, o = map(int, input().split())
    tmp = check[-1] + (o-i)
    check.append(tmp)

print(max(check))