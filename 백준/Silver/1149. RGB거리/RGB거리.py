import sys
input = sys.stdin.readline

n = int(input())

scores = [[0, 0, 0] for i in range(n)]
graph = [list(map(int, input().split())) for i in range(n)]
#print(graph)

for i in range(n) :
    if i == 0 :
        scores[i] = graph[i]
    else :
        scores[i][0] = min(scores[i - 1][1], scores[i - 1][2]) + graph[i][0]
        scores[i][1] = min(scores[i - 1][0], scores[i - 1][2]) + graph[i][1]
        scores[i][2] = min(scores[i - 1][0], scores[i - 1][1]) + graph[i][2]

print(min(scores[-1]))