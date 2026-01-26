from collections import Counter

def solution(topping):
    answer = 0
    tmp1 = dict(Counter(topping))
    tmp2 = {i:0 for i in topping}
    
    s1 = len(tmp2)
    s2 = 0
        
    for cake in topping :
        tmp1[cake] -= 1
        tmp2[cake] += 1
        
        if tmp1[cake] == 0 :
            s1 -= 1
        if tmp2[cake] == 1 :
            s2 += 1
        if s1 == s2 :
            answer += 1
    return answer