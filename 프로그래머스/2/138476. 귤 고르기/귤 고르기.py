def solution(k, tangerine):
    dict = {}
    answer = []
    for i in tangerine :
        if i in dict :
            dict[i] += 1
        else :
            dict[i] = 1
        
    for i in dict :
        answer.append(dict[i])
        
    answer.sort(reverse=True)
    result = 0
    num = 0
    for i in answer :
        result += i
        num += 1
        if result >= k :
            break
    return num
        
    
