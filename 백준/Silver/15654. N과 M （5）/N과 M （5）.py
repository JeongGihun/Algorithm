import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
visit = [False for i in range(len(l))]
l.sort()
stack = []

def ref(x) :
    if x == m :
        print(' '.join(map(str, stack)))
        return
    for i in range(len(l)):
        if not visit[i] :
            visit[i] = True
            stack.append(l[i])
            ref(x+1)
            stack.pop()
            visit[i] = False

ref(0)

