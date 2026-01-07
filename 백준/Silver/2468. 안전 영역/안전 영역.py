from collections import deque
import sys
input = sys.stdin.readline

num = int(input())
origin = [list(map(int, input().split())) for i in range(num)]

q = deque([])
rain = 0
d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]
stack = []
while True :
    # graph 조정
    graph = [[0] * num for i in range(num)]
    for i in range(num) :
        for j in range(num) :
            if origin[i][j] > rain :
                graph[i][j] = 1
            else :
                graph[i][j] = 0
    # visit 작성
    visit = [[False] * num for i in range(num)]
    q = deque([])
    island = 0    # island는 섬 갯수 확인용
    for i in range(num) :
        for j in range(num) :
            if graph[i][j] == 1 and not visit[i][j] :
                q.append([i, j])
                visit[i][j] = True
                island += 1
                while q :
                    x, y = q.popleft()
                    for k in range(4) :
                        nx = x + d_x[k]
                        ny = y + d_y[k]
                        if 0 <= nx < num and 0 <= ny < num :
                            if graph[nx][ny] == 1 and not visit[nx][ny] :
                                q.append([nx, ny])
                                visit[nx][ny] = True
    stack.append(island)
    rain += 1
    if island == 0 :
        break
print(max(stack))
