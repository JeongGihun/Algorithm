import sys
input = sys.stdin.readline
num = int(input())
stack = []
ans = 0
for i in range(num) :
    s, e = list(map(int, input().split()))
    stack.append([s, e])

stack.sort(key= lambda x : (x[1], x[0]))
check = 0
for i in stack :
    if check <= i[0] :
        ans += 1
        check = i[1]
        #print(i)
print(ans)