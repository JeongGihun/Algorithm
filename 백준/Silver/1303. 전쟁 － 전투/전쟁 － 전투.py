import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visit = [[False] * n for _ in range(m)]
dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
W, B = 0, 0
q = deque([])

for j in range(m) :
    for i in range(n) :
        if not visit[j][i] :
            q.append([i, j])
            tmp = 1
            now = ''
            while q :
                x, y = q.pop()
                now = graph[y][x]
                visit[y][x] = True
                for dx, dy in dir :
                    if 0 <= x+dx < n and 0 <= y+dy < m :
                        if not visit[y+dy][x+dx] and graph[y+dy][x+dx] == now :
                            visit[y+dy][x+dx] = True
                            tmp += 1
                            q.append([x+dx, y+dy])
            if now == "W" :
                W += pow(tmp, 2)
            if now == "B" :
                B += pow(tmp, 2)
print(W, B)