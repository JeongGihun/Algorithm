import sys
input = sys.stdin.readline

d_x = [1, -1, 0, 0, 1, 1, -1, -1]
d_y = [0, 0, 1, -1, 1, -1, 1, -1]

while True :
    n, m = map(int, input().split())
    if n==0 and m==0 :
        break

    ans = 0
    stack = []
    graph = [list(map(int, input().split())) for _ in range(m)]
    visit = [[False] * n for _ in range(m)]

    for j in range(m) :
        for i in range(n) :
            if not visit[j][i] and graph[j][i] == 1 :
                stack.append([j, i])
                visit[j][i] = True
                ans += 1
                while stack :
                    y, x = stack.pop()
                    for dir in range(8) :
                        nx = x + d_x[dir]
                        ny = y + d_y[dir]
                        if 0 <= nx < n and 0 <= ny < m :
                            if not visit[ny][nx] and graph[ny][nx] == 1 :
                                stack.append([ny, nx])
                                visit[ny][nx] = True
    print(ans)