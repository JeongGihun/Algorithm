from collections import deque
import sys
input = sys.stdin.readline

people = int(input())
s, e = map(int, input().split())
num = int(input())
visit = [False] * (people+1)
graph = [[] for i in range(people+1)]
for i in range(num) :
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

q = deque([[s, 0]])
visit[s] = True
while q :
    tmp, cnt = q.popleft()
    if tmp == e :
        print(cnt)
        break
    for i in graph[tmp] :
        if not visit[i] :
            visit[i] = True
            q.append([i, cnt+1])
else :
    print(-1)