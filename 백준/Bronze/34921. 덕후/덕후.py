import sys
input = sys.stdin.readline

a, t = map(int, input().split())
ans = 10 + 2 * (25-a+t)
print(ans if ans >= 0 else 0)