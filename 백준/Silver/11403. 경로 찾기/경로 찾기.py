import sys
input = sys.stdin.readline

num = int(input())
graph = [list(map(int, input().split())) for _ in range(num)]

for k in range(num) :
    for j in range(num) :
        for i in range(num) :
            if graph[i][k] == 1 and graph[k][j] :
                graph[i][j] = 1

for l in graph :
    print(' '.join(map(str, l)))