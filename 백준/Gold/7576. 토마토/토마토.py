from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visit = [[False] * n for _ in range(m)]

d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]

q = deque([])
ans = 0
flag = True
for i in range(n) :
    for j in range(m) :
        if not visit[j][i] and graph[j][i] == 1 :
            q.append([j, i, 1])

while q :
    y, x, num = q.popleft()
    visit[y][x] = True
    for dir in range(4) :
        nx = x + d_x[dir]
        ny = y + d_y[dir]
        if 0 <= nx < n and 0 <= ny < m :
            if not visit[ny][nx] and graph[ny][nx] == 0 :
                graph[ny][nx] = 1
                q.append([ny, nx, num+1])
                ans = num

for i in range(n) :
    for j in range(m) :
        if graph[j][i] == 0 :
            flag = False

if flag :
    print(ans)
else :
    print(-1)