def solution(strings, n):
    answer = []
    
    for i in strings :
        answer.append([i[n], i])
    answer.sort()
    result = list(map(lambda x : x[1], answer))
    
    
    return result