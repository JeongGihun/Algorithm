import string
def solution(s):
    answer = []
    where = {chr(i): -1 for i in range(ord('a'), ord('z')+1)}
    
    for i in range(len(s)) :
        if where[s[i]] == -1 :
            answer.append(where[s[i]])
        else :
            answer.append(i+1 - where[s[i]])
        where[s[i]] = i+1
    
    return answer