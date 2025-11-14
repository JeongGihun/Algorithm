def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    check_budget = 0
    while d :
        check_budget += d.pop()
        if check_budget > budget :
            break
        answer += 1
        
    
    return answer