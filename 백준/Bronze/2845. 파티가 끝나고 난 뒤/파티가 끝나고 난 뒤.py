import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = ''

check = n * m

for i in l :
    ans += (str(i-check))
    ans += ' '

print(ans)