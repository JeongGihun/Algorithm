import sys
input = sys.stdin.readline

n = int(input())
rec = []
ans = [0 for i in range(n)]
for i in range(n) :
    tmp = list(map(int, input().split()))
    rec.append(tmp)

for i in range(n) :
    tmp = rec.pop()
    if i == 0 :
        ans = tmp
        continue
    for j in range(len(tmp)) :
        ans[j] = max(ans[j]+tmp[j], ans[j+1]+tmp[j])

print(ans[0])