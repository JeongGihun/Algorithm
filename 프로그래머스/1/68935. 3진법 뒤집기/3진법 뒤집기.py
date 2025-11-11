def solution(n):
    answer = []
    if n < 3 :
        answer.append(str(n))
    while n >= 3:
        tmp = (n%3)
        answer.append(str(tmp))
        n //= 3
        if n < 3 :
            answer.append(str(n))
            
    result = 0
    num = 0
    for i in range(len(answer)-1, -1, -1) :
        result += int(answer[i]) * pow(3, num)
        num += 1

    
    return result