from collections import deque
import sys
input = sys.stdin.readline

row, col, hei = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(col)] for _2 in range(hei)]

q = deque([])
d_x = [1, -1, 0, 0, 0, 0]
d_y = [0, 0, 1, -1, 0, 0]
d_z = [0, 0, 0, 0, 1, -1]
ans = -1
for z in range(hei) :
    for y in range(col) :
        for x in range(row) :
            if graph[z][y][x] == 1 :
                q.append([z, y, x, 0])

while q :
    z, y, x, num = q.popleft()

    for dir in range(6) :
        nx = x + d_x[dir]
        ny = y + d_y[dir]
        nz = z + d_z[dir]
        if 0 <= nx < row and 0 <= ny < col and 0 <= nz < hei :
            if graph[nz][ny][nx] == 0 :
                graph[nz][ny][nx] = 1
                q.append([nz, ny, nx, num+1])
    ans = num

flag = any(0 in row for hei in graph for row in hei)
ans = -1 if flag else ans
print(ans)
