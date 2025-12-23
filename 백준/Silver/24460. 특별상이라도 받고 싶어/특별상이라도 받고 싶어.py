import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

num = int(input())
graph = [list(map(int, input().split())) for i in range(num)]

def rep(x, y, n) : # x는 수, n은 현재 크기
    if n == 1 :
        return graph[x][y]
    half = n//2
    tmp = [rep(x, y, half), rep(x+half, y, half), rep(x, y+half, half), rep(x+half, y+half, half)]
    tmp.sort()
    return tmp[1]

print(rep(0, 0, num))