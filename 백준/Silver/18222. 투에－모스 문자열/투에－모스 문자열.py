import sys
input = sys.stdin.readline

num = int(input())

num = bin(num-1)[2:]

ans = num.count("1")

if ans % 2 == 0 :
    print("0")
else :
    print("1")
