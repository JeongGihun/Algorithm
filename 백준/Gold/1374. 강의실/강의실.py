import sys
import heapq
input = sys.stdin.readline

n = int(input())
l = []
max_ = 0
c = 0
for _ in range(n) :
    check, s, e = map(int, input().split())
    heapq.heappush(l, [s, 1])
    heapq.heappush(l, [e, -1])

while l :
    tmp = heapq.heappop(l)
    c += tmp[1]
    max_ = max(max_, c)
print(max_)
