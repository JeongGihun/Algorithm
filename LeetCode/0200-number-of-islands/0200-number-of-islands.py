class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        fx, fy = len(grid[0]), len(grid)
        visit = [[False] * fx for i in range(fy)]
        q = deque()

        dx = [1, -1, 0, 0]
        dy = [0 , 0, 1, -1]
        ans = 0
        for j in range(fy) :
            for i in range(fx) :
                if grid[j][i] == "1" and visit[j][i] == False :
                    q.append([j, i])
                    visit[j][i] = True
                    ans += 1
                    while q :
                        y, x = q.pop()
                        for k in range(4) :
                            if 0 <= x+dx[k] < fx and 0 <= y+dy[k] < fy and visit[y+dy[k]][x+dx[k]] == False and grid[y+dy[k]][x+dx[k]] == "1" :
                                q.append([y+dy[k], x+dx[k]])
                                visit[y+dy[k]][x+dx[k]] = True
        

        return ans