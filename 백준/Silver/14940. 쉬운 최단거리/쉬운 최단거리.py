from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
visit = [[False for i in range(m)] for j in range(n)]
ans = [[-1 for i in range(m)] for j in range(n)]

q = deque([])
d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            ans[i][j] = 0
        elif graph[i][j] == 2 :
            q.append([i, j])
            visit[i][j] = True
            ans[i][j] = 0
            while q :
                x, y = q.popleft()
                for k in range(4) :
                    nx = x + d_x[k]
                    ny = y + d_y[k]
                    if 0 <= nx < n and 0 <= ny < m :
                        if not visit[nx][ny] and graph[nx][ny] == 1:
                            q.append([nx, ny])
                            visit[nx][ny] = True
                            ans[nx][ny] = ans[x][y] + 1

for i in ans :
    for j in i :
        print(j, end =' ')
    print()
