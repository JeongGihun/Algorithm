from collections import deque
def solution(order):
    origin = [i+1 for i in range(len(order))]
    order = deque(order)
    stack = []
    ans = 0
    
    for num in origin :
        stack.append(num)
        while stack and order :
            if stack[-1] == order[0] :
                ans += 1
                stack.pop()
                order.popleft()
            else:
                break
            
    
    return ans