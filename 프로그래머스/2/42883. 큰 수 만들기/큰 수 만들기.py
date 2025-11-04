def solution(number, k):
    answer = ''
    l = list(map(int, number))
    stack = []
    num = 0
    
    for i in range(len(l)) :
        tmp = l[i]
        while stack and stack[-1] < tmp and num < k :
            stack.pop()  
            num += 1
        stack.append(tmp)
        
    if num < k :
        stack = stack[:-(k-num)]
    
    for i in stack :
        answer += str(i)
        
    return answer