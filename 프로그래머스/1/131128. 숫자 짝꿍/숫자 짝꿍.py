from collections import Counter
def solution(X, Y):
    answer = ''
    tmpx = Counter(X)
    tmpy = Counter(Y)
    for i in range(9, -1, -1) :
        answer += str(i) * min(tmpx[str(i)], tmpy[str(i)])
    
    if not answer :
        return "-1"
    
    if answer[0] == "0" :
        return "0"
    
    return answer