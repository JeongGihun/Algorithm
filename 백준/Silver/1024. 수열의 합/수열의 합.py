import sys
input = sys.stdin.readline

n, l = map(int, input().split())
ans = -1
while l <= 100 :
    if (2 * n) % l == 0 :
        tmp = (2*n) // l + 1 - l
        if tmp % 2 == 0 and tmp > -1 :
            ans = int(tmp//2)
            break
    l += 1

print(ans if ans==-1 else ' '.join([str(n) for n in range(ans, ans+l)]))