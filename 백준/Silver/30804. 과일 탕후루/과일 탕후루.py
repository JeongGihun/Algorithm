import sys

input = sys.stdin.readline

n = input()
l = list(map(int, input().split()))
check = dict()
s, e = 0, 0
max_n = 0
while e < len(l) :
    if l[e] not in check.keys():
        check[l[e]] = 0

    if len(check) < 3 :
        check[l[e]] += 1
        max_n = max(max_n, e - s + 1)
        e += 1
    else:
        check[l[s]] -= 1
        if check[l[s]] == 0:
            del check[l[s]]
        s += 1

    #print(s, e, max_n, check)

print(max_n)