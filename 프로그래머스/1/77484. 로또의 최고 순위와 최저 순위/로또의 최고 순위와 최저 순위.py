def solution(lottos, win_nums):
    answer = []
    num = lottos.count(0)
    check = 7
    for i in lottos :
        if i == 0:
            continue
        else :
            for j in win_nums :
                if i==j :
                    check -= 1
                    
    if check-num > 6 :
        answer.append(6)
    else:
        answer.append(check-num)                
    if check > 6 :
        answer.append(6)
    else:
        answer.append(check)
    
    return answer