import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n 나무 갯수 / m은 필요한 나무 높이
l = list(map(int, input().split())) # 나무
s, e = 0, max(l)
ans = 0

while s <= e :
    mid = (s + e) // 2
    total = 0
    for i in l :
        if i > mid :
            total += (i-mid)
            if total >= m :
                break

    if total >= m :
        ans = mid
        s = mid + 1
    else :
        e = mid - 1
print(ans)
