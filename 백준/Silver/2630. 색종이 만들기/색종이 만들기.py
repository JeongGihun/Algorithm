import sys

input = sys.stdin.readline

num = int(input())
graph = [list(map(int, input().split())) for i in range(num)]
ans = {'0': 0, '1': 0}

def check(c_x, c_y, c_n):
    for i in range(c_n):
        for j in range(c_n):
            if graph[c_x + i][c_y + j] != graph[c_x][c_y]:
                return False
    return True

def rep(x, y, n):
    if check(x, y, n):
        ans[str(graph[x][y])] += 1
    else:
        for i in range(2):
            for j in range(2):
                rep(x + i * n // 2, y + j * n // 2, n // 2)


rep(0, 0, num)

print(ans['0'])
print(ans['1'])