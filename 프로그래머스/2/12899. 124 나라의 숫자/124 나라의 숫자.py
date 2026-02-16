def solution(n):
    answer = ''
    s = {0 : "1", 1 : "2", 2 : "4"}
    l = []
    while n != 0 :
        tmp = n % 3
        n //= 3
        if tmp == 0 :
            answer = "4" + answer
            n -= 1
        else :
            answer = str(tmp) + answer
    
    return answer