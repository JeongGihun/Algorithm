import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]
visit = [[False] *n for _ in range(n)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, s) :
    visit[y][x] = True
    for d_x, d_y in dirs :
        nx = x + d_x
        ny = y + d_y
        if 0 <= nx < n and 0 <= ny < n :
            if not visit[ny][nx] and graph[ny][nx] == s :
                dfs(nx, ny, s)


ans = [0, 0]
for i in range(n) :
    for j in range(n) :
        if not visit[j][i] :
            tmp = graph[j][i]
            dfs(i, j, tmp)
            ans[0] += 1

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == "G":
            graph[i][j] = "R"
visit = [[False] *n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if not visit[j][i] :
            tmp = graph[j][i]
            dfs(i, j, tmp)
            ans[1] += 1

print(ans[0], ans[1])
