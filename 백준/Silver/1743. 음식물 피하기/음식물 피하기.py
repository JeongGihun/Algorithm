import sys
input = sys.stdin.readline

n, m, trash = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visit = [[False] *m for _ in range(n)]

for i in range(trash) :
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    graph[y][x] = 1

stack = []
list_trash = []
d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]

for i in range(n) :
    for j in range(m) :
        if not visit[i][j] and graph[i][j] == 1 :
            stack.append([i, j])
            ans = 1
            while stack :
                y, x = stack.pop()
                visit[y][x] = True
                for dir in range(4) :
                    nx = x + d_x[dir]
                    ny = y + d_y[dir]
                    if 0 <= nx < m and 0 <= ny < n :
                        if not visit[ny][nx] and graph[ny][nx] == 1 :
                            stack.append([ny, nx])
                            visit[ny][nx] = True
                            ans += 1
            list_trash.append(ans)
print(0 if len(list_trash) == 0 else max(list_trash))
