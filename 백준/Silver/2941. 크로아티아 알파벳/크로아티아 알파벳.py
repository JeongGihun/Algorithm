import sys
input = sys.stdin.readline

sen = input().rstrip()
cro = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}
num = 0
while sen :
    if sen[:2] in cro :
        num += 1
        sen = sen[2:]
    elif sen[:3] in cro :
        num += 1
        sen = sen[3:]
    else :
        num += 1
        sen = sen[1:]

print(num)