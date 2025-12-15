import sys

input = sys.stdin.readline

def rep(n, x) :

    if n == 0 :

        print("-", end ='')

        return 

        

    rep(n-1, x)

    print(" "*pow(3, n-1), end='')

    rep(n-1, x)

while True :

    try :

        num = int(input())

        rep(num, num)

        print()

    except :

        break