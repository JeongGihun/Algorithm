import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def check(a, b) :

    if a ==0 or b == 0 :

        return 0

    if a == b :

        return 1

    if a < b :

        a, b = b, a

    num = a//b    

    a, b = a%b, b

    return num+check(a, b)    

        

num = check(n, m)

print(num)