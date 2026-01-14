import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

stack = []
check = [] # 갯수와 넓이 확인
d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]
for i in range(n) :
    for j in range(m) :
        if not visit[i][j] and graph[i][j] == 1 :
            tmp = 1
            stack.append([i, j])
            visit[i][j] = True

            while stack :
                y, x = stack.pop()

                for dir in range(4) :
                    nx = x + d_x[dir]
                    ny = y + d_y[dir]
                    if 0 <= nx < m and 0 <=ny < n :
                        if not visit[ny][nx] and graph[ny][nx] == 1 :
                            stack.append([ny, nx])
                            visit[ny][nx] = True
                            tmp += 1
            check.append(tmp)


print(len(check))
print(max(check) if len(check) > 0 else 0)