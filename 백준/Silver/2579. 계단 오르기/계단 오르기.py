import sys
input = sys.stdin.readline

n = int(input())
l = []
scores = [[0, 0] for _ in range(n)]
for _ in range(n) :
    l.append(int(input()))

for i in range(n) :
    if i == 0 :
        scores[i][0] = l[0]
        continue
    if i == 1 :
        scores[i][0] = l[1]
        scores[i][1] = scores[0][0] + l[1]
        continue

    scores[i][0] = max(scores[i-2][1], scores[i-2][0]) + l[i]
    scores[i][1] = scores[i-1][0] + l[i]

print(max(scores[-1][0], scores[-1][1]))