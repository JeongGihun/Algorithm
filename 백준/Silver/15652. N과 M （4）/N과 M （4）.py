import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p =[]
def ref(x) :
    if len(p) == m :
        print(' '.join(map(str, p)))
        return

    for i in range(x, n+1) :
        p.append(i)
        ref(i)
        p.pop()

ref(1)