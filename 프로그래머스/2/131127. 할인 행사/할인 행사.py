

def solution(want, number, discount):
    answer = 0
    l = discount[:10]
    dic = {}
    for i in range(len(want)) :
        dic[want[i]] = number[i]
    
    # 일단 초기 설정
    for i in range(len(l)) :
        if l[i] in dic :
            dic[l[i]] -= 1
    for j in dic :
        if dic[j] > 0 :
            break
    else :
        answer +=1        
            
    
    # 슬라이딩 윈도우로 확인. 이후 DIC확인
    for i in range(10, len(discount)) :
        if discount[i-10] in dic :
            dic[discount[i-10]] += 1
        if discount[i] in dic :
            dic[discount[i]] -= 1
        #print(dic)    
        for j in dic :
            if dic[j] > 0 :
                break
        else :
            answer +=1
    
    return answer