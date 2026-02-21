import sys
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 지역수, 수색범위, 길의 개수
l = list(map(int, input().split())) # 아이템의 갯수
check = []
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1) :
    graph[i][i] = 0

for _ in range(r) :
    i, j, k = map(int, input().split())
    graph[i][j] = min(k, graph[i][j])
    graph[j][i] = min(k, graph[j][i])

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for j in range(1, n+1) :
    tmp = 0
    for i in range(1, n+1) :
        if graph[j][i] <= m :
            tmp += l[i-1]
    check.append(tmp)
print(max(check))