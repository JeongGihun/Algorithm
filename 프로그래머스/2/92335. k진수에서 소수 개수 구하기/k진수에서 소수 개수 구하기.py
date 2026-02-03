import math
def solution(n, k):
    ans = 0
    num = ''
    while n > 0 :
        num = str(n%k) + num
        n = n//k
    checks = num.split('0')
    for check in checks :
        if check == '' :
            continue
        tmp = int(check)
        if tmp < 2 :
            continue
        for i in range(2, math.floor(math.sqrt(tmp))+1) :
            if tmp % i == 0:
                break
        else :
            ans += 1
    
    return ans