import sys

input = sys.stdin.readline

def rep(x, y, n) :

    if n == 2 :

        return sorted([graph[x][y], graph[x+1][y], graph[x][y+1], graph[x+1][y+1]])[-2]

    a=rep(x, y, n//2)

    b=rep(x, y+n//2, n//2)

    c=rep(x+n//2, y, n//2)

    d=rep(x+n//2, y+n//2, n//2)

    return sorted([a, b, c, d])[-2]

num = int(input())

graph = [list(map(int, input().split())) for i in range(num)]

print(rep(0,0,num))