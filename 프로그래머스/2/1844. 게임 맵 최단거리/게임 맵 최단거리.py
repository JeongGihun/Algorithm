from collections import deque

def bfs(graph) :
    n = len(graph[0])
    m = len(graph)
    visit = [[False for i in range(n)] for j in range(m)]
    q = deque([[0, 0, 1]])
    visit[0][0] = True
    d_x = [1, -1, 0 ,0]
    d_y = [0, 0, 1, -1]
    
    while q :
        x, y, cnt = q.popleft()
        if x == m-1 and y == n-1 :
            return cnt
        for i in range(4) :
            nx = x + d_x[i]
            ny = y + d_y[i]
            if 0 <= nx < m and 0 <= ny < n :
                if not visit[nx][ny] and graph[nx][ny] == 1 :
                    q.append([nx, ny, cnt+1])
                    visit[nx][ny] = True
    return -1
                
def solution(maps):
    stack = []
    graph = maps
    num = 0
    answer = bfs(graph)
    return answer