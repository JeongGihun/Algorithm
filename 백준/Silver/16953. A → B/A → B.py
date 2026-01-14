import sys
input = sys.stdin.readline

s, e = map(int, input().split())
check = 0

while e > s :
    tmp = str(e)
    if tmp[-1] == "1" :
        e = int(tmp[:-1])
        check += 1
    elif e % 2 == 0 :
        e //= 2
        check += 1
    else :
        break

if s == e :
    print(check+1)
else :
    print(-1)