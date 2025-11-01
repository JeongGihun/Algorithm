def solution(s):
    answer = ''
    l = list(map(str, s.split()))
    
    for i in range(len(l)) :
        l[i] = int(l[i])
    
    answer += str(min(l))
    answer += ' '
    answer += str(max(l))
    
    return answer