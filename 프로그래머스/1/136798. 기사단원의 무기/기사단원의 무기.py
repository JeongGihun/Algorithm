import math
def solution(number, limit, power):
    answer = 0
    l = [0 for i in range(number+1)]
    for i in range(1, number+1) :
        cnt = 0
        for j in range(1, int(math.sqrt(i))+1) :
            if i % j == 0 :
                if j*j == i :
                    cnt += 1
                else :
                    cnt += 2
        l[i] = power if cnt > limit else cnt
    
    return sum(l)