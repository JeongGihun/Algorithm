import sys
input = sys.stdin.readline

num = int(input())
graph = [list(map(int, input().split())) for j in range(num)]
count = {0:0, 1:0, -1:0}
def check(s_x, s_y, size) :  # size는 사이즈, n은 들어가는 값
    for i in range(size) :
        for j in range(size) :
            if graph[s_x+i][s_y+j] != graph[s_x][s_y] :
                return False
    else :
        return True

def rep(x, y, n) :
    if check (x, y, n) :
        count[graph[x][y]] += 1
    else :
        rep(x, y, n//3)
        rep(x, y+n//3, n//3)
        rep(x, y+n*2//3, n//3)
        rep(x+n//3, y, n//3)
        rep(x+n//3, y+n//3, n//3)
        rep(x+n//3, y+n*2//3, n//3)
        rep(x+n*2//3, y, n//3)
        rep(x+n*2//3, y+n//3, n//3)
        rep(x+n*2//3, y+n*2//3, n//3)

rep(0, 0, num)

print(count[-1])
print(count[0])
print(count[1])