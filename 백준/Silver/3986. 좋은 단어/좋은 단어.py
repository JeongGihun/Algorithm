import sys
input = sys.stdin.readline

num = int(input())
result = 0
for i in range(num) :
    l = list(input().strip()) # 입력 리스트
    tmp = [] # 아치 구조인지 판별하기 위한 임시 리스트
    tmp.append(l.pop()) # tmp에 l의 마지막 값 입력

    while l :
        if len(tmp) == 0 :
            tmp.append(l.pop())
        elif l[-1] == tmp[-1] :
            l.pop()
            tmp.pop()
        elif l[-1] != tmp[-1] :
            tmp.append(l.pop())
        else :
            break

    if not l and not tmp :
        result += 1

print(result)