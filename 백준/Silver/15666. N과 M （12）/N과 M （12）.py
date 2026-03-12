import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
rml = []
prev = None

l.sort()
# 중복 수열 제거
for i in l :
    if i == prev :
        continue
    rml.append(i)
    prev = i

ans = []
def ref(x, s) :
    if x == m :
        print(' '.join(map(str, ans)))
        return
    for i in range(s, len(rml)) :
        ans.append(rml[i])
        ref(x+1, i)
        ans.pop()


ref(0, 0)