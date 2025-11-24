from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    num = (sum(queue1) + sum(queue2)) // 2
    check = len(queue1) + len(queue2) # 최대 도는 횟수
    compare = sum(queue1)
    while True :
        if compare == num :
            break
        elif compare > num :
            compare -= q1[0]
            q2.append(q1.popleft())
            
        elif compare < num :
            compare += q2[0]
            q1.append(q2.popleft())
        
        answer += 1
        
        if answer > 2 * check :
            answer = -1
            break  
            
    return answer