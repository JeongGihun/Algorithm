import sys
input = sys.stdin.readline

n = int(input())
d_x = dict()
d_y = dict()
for _ in range(n) :
    k, v = map(int, input().split())
    d_x[k] = d_x.get(k, 0) + 1
    d_y[v] = d_y.get(v, 0) + 1

ans = 0

for i in d_x.values() :
    if i > 1 :
        ans += 1

for i in d_y.values() :
    if i > 1 :
        ans +=1

print(ans)