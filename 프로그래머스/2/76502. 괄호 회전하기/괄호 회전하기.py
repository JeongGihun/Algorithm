from collections import deque

def solution(s):
    answer = 0
    q = deque(list(s))
    dic = {}
    dic[')'] = '('
    dic['}'] = '{'
    dic[']'] = '['
    
    for i in range(len(s)) :
        tmp = list(q) # 해당 순환의 list 복사
        stack = []
        while tmp :
            if tmp[-1] in '([{' :
                if not stack :
                    break
                elif dic[stack[-1]] == tmp[-1] :
                    stack.pop()
                    tmp.pop()
                else :
                    break
            else :
                stack.append(tmp.pop())
            
        if not stack and not tmp :
            answer += 1
        q.rotate(1)
    
    return answer