from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visit = [False] * (F+1)
ans = [0] * (F+1)

queue = deque([S])
visit[S] = True

while queue:
    tmp = queue.popleft()

    for now in (tmp + U, tmp - D):
        if 1 <= now <= F and not visit[now]:
            visit[now] = True
            ans[now] = ans[tmp] + 1
            queue.append(now)

if visit[G]:
    print(ans[G])
else:
    print("use the stairs")