def solution(sequence, k):
    answer = []
    s, e = 0, 0
    num = sequence[0]
    while s <= e and e < len(sequence) :
        if num == k :
            answer.append([e-s, s, e])
            e += 1
            if e < len(sequence) :
                num += sequence[e]
        elif num < k :
            e += 1
            if e < len(sequence) :
                num += sequence[e]
        else :
            num -= sequence[s]
            s += 1  
    answer.sort()
    
    return answer[0][1:]