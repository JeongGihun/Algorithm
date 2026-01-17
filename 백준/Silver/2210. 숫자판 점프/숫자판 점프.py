import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

graph = [list(map(int, input().split())) for _ in range(5)]
num_list = set()

def dfs(y, x, s) :
    s += str(graph[y][x])
    if len(s) == 6 :
        num_list.add(s)
        return
    for dx, dy in dir :
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5 :
            dfs(ny, nx, s)

number = ''
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for j in range(5) :
    for i in range(5) :
        dfs(i, j, number)

print(len(num_list))