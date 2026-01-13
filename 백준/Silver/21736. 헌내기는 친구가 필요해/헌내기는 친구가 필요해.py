import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]

stack = []
friend = 0
for y in range(n) :
    for x in range(m) :
        if graph[y][x] == 'I' :
            stack.append([y, x])

while stack :
    y, x = stack.pop()
    visit[y][x] = True

    for dir in range(4) :
        nx = x + d_x[dir]
        ny = y + d_y[dir]
        if 0 <= nx < m and 0 <= ny < n :
            if not visit[ny][nx] and graph[ny][nx] != 'X' :
                stack.append([ny, nx])
                visit[ny][nx] = True
                if graph[ny][nx] == 'P' :
                    friend += 1

friend = 'TT' if friend==0 else friend
print(friend)