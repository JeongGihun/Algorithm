from collections import deque
def solution(numbers, target):
    answer = 0
    check = [[0]]
    for i in numbers :
        tmp = []
        for j in check[-1] :
            tmp.append(j+i)
            tmp.append(j-i)
        check.append(tmp)
        
    result = check[-1].count(target)
    return result