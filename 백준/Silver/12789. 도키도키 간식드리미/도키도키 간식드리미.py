import sys
input = sys.stdin.readline

num = int(input())
l = list(map(int, input().split()))
l.reverse()
stack = []
check = 1
flag = True

while check != num :
    if l and l[-1] == check :
        l.pop()
        check += 1
    elif stack and stack[-1] == check :
        stack.pop()
        check += 1
    else :
        if l :
            stack.append(l.pop())
        else :
            flag = False
            break

if flag :
    print("Nice")
else :
    print("Sad")

