import sys

input = sys.stdin.readline

city = int(input())
INF = int(1e9)
graph = [[INF] * (city + 1) for _ in range(city + 1)]
n = int(input())

for i in range(1, city + 1):
    graph[i][i] = 0

for _ in range(n):
    i, j, k = map(int, input().split())
    graph[i][j] = min(k, graph[i][j])

for k in range(1, city + 1):
    for i in range(1, city + 1):
        for j in range(1, city + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, city + 1):
    for j in range(1, city + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, city+1) :
    print(' '.join(map(str, graph[i][1:])))