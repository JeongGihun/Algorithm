import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n 나무 갯수 / m은 필요한 나무 높이
l = list(map(int, input().split())) # 나무
l.sort(reverse=True)

x = 0 # 위치
cnt = 1 # 계산하는 수량
while m > 0 :
    if x == n-1 or l[x] > l[x+1] :
        l[x] -= 1
        m -= cnt
    else :
        cnt += 1
        x += 1

print(l[x])
