from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [list(map(int, input().strip())) for i in range(n)]
visit = [[False for j in range(m)] for i in range(n)]
# n이 y / m이 x
q = deque([[0, 0, 1]])
visit[0][0] = True
d_y = [1, -1, 0, 0]
d_x = [0, 0, 1, -1]

while q :
    y, x, cnt = q.popleft()

    if x == m-1 and y == n-1 :
        print(cnt)
        break

    for i in range(4) :
        nx = x + d_x[i]
        ny = y + d_y[i]

        if 0 <= nx < m and 0 <= ny < n :
            if not visit[ny][nx] and graph[ny][nx] == 1 :
                visit[ny][nx] = True
                q.append([ny, nx, cnt+1])
