import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0 for i in range(m+1)]
road = []
for _ in range(n) :
    s, e, long = map(int, input().split())
    if e <= m and e - s > long :
        road.append([s, e, long])

for i in range(1, m+1) :
    dp[i] = dp[i-1] + 1
    for x, y, long in road :
        if y == i :
            dp[i] = min(dp[i], dp[x]+long)

print(dp[-1])