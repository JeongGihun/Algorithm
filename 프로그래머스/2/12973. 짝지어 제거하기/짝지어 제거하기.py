def solution(s):
    answer = 0
    l = list(s)
    stack = []
    while l :
        if not stack :
            stack.append(l.pop())
        elif stack[-1] == l[-1] :
            stack.pop()
            l.pop()
        else :
            stack.append(l.pop())
            
    if stack :
        answer = 0
    else :
        answer = 1

    return answer