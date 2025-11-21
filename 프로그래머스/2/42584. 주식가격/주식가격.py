def solution(prices):
    answer = [0 for i in prices]
    stack = []
    for i in range(len(prices)) :
        while stack :
            if prices[stack[-1]] > prices[i] :
                tmp = stack.pop()
                answer[tmp] = i-tmp
            else :
                break
        stack.append(i)   
    
    for i in stack :
        answer[i] = len(prices)-i-1
    return answer