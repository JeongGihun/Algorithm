def solution(s):
    answer = 0
    l = list(s)
    num = [0, 0]
    check_str = ''
    for i in l :
        if num[0] == 0 :
            check_str = i
            num[0] += 1
            
        elif check_str == i :
            num[0] += 1
        else :
            num[1] += 1
        
        if num[0] == num[1] :
            num[0], num[1] = 0, 0
            check_str = ''
            answer += 1
            
    if num[0] > 0 :
        answer += 1
    return answer