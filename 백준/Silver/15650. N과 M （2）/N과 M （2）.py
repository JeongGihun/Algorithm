import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = []
def ref(check) :
    if len(p) == m :
        print(' '.join(map(str, p)))
        return

    for i in range(check, n+1) :
        p.append(i)
        ref(i+1)
        p.pop()

ref(1)