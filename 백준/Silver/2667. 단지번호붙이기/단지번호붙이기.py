from collections import deque

import sys

input = sys.stdin.readline



big = int(input())

graph = [list(map(int, input().strip())) for i in range(big)]

visit = [[False] * big for i in range(big)]

q = deque([])

stack = []

d_x = [1, -1, 0, 0]

d_y = [0, 0, 1, -1]



for i in range(big) :

    for j in range(big) :

        if graph[i][j] == 1 and visit[i][j] == False :

            q.append([i, j])

            visit[i][j] = True

            num = 1

            while q :

                x, y = q.popleft()

                for k in range(4) :

                    nx = x + d_x[k]

                    ny = y + d_y[k]

                    if 0 <= nx < big and 0 <= ny < big :

                        if graph[nx][ny] == 1 and visit[nx][ny] == False :

                            q.append([nx, ny])

                            visit[nx][ny] = True

                            num += 1

            stack.append(num)

stack.sort()

print(len(stack))

for i in stack :

    print(i)