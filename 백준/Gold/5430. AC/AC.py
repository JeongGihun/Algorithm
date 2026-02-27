import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    check = list(input().rstrip())
    n = int(input())
    l = list(input().split(","))
    q = deque(l)
    q[0] = q[0][1:]
    q[-1] = q[-1][:-2]
    flag = True
    if len(q) == 1 and q[0] == "" :
        q.pop()
    for i in check:
        if i == "R":
            flag = not flag
        elif i == "D":
            if q :
                if flag :
                    q.popleft()
                else :
                    q.pop()
            else :
                print("error")
                break
    else :
        if not flag :
            q.reverse()
        print("["+",".join(q)+"]")


