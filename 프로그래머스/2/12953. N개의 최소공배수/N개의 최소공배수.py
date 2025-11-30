from collections import deque
def solution(arr):
    q = deque(arr)
    
    while len(q) != 1 :
        num1 = q.popleft()
        num2 = q.popleft()
        # 2개의 수를 뺀다
        div = 1
        
        if num1 > num2 :
            num1, num2 = num2, num1
        # 작은수를 num1으로 하겠다
        
        for i in range(num1, 0, -1) :
            if num1 % i == 0 and num2 % i == 0 :
                q.appendleft(num1*num2//i)
                break
        
    answer = q.pop()
    return answer