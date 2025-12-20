def solution(n):
    stack = []
    for i in range(1, n+1) :
        if i % 2 == 1 :
            stack.append(i)
    
    return stack