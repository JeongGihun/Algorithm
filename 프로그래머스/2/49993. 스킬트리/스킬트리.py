from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees :
        check = deque(skill)
        tmp = list(tree)
        for i in tmp :
            if i in check :
                if check[0] == i :
                    check.popleft()
                else :
                    break
        else :
            
            answer += 1
    
    return answer