import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
n = pow(2, n)
# 그래프 채우기
check = 0
def ref(s, x, y, num) :
    if x==c and y==r :
        print(num)
        return
# 3, r=7, c=7
    tmp = s//2
    if x+tmp > c and y+tmp > r :
        ref(tmp, x, y, num)
    elif x+tmp <= c and y+tmp > r :
        ref(tmp, x + tmp, y + 0, num + pow(tmp, 2))
    elif x+tmp > c and y+tmp <= r :
        ref(tmp, x + 0, y + tmp, num + pow(tmp, 2) * 2)
    else :
        ref(tmp, x + tmp, y + tmp, num + pow(tmp, 2) * 3)

ref(n, 0, 0, check)
