import sys
input = sys.stdin.readline

num = int(input())
l = list(map(int, input().split()))

tmp = sorted(l)
dic = dict()
dic[tmp[0]] = 0
for i in range(1, len(tmp)) :
    if tmp[i] == tmp[i-1] :
        dic[tmp[i]] = dic[tmp[i-1]]
    else :
        dic[tmp[i]] = dic[tmp[i-1]] + 1

for i in l :
    print(dic[i], end=' ')