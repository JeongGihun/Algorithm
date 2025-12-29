import sys
input = sys.stdin.readline

num = int(input())

for i in range(num) :
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    d_x = pow(x1-x2, 2)
    d_y = pow(y1-y2, 2)
    d_r = pow(r1+r2, 2)
    d_r2 = pow(r1-r2, 2)

    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    else :
        if d_x + d_y < d_r2 :
            print(0)
        elif d_x + d_y == d_r2 :
            print(1)
        elif d_x + d_y == d_r :
            print(1)
        elif d_x + d_y > d_r :
            print(0)
        else :
            print(2)

