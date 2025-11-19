from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight = 0
    q = deque([0 for i in range(bridge_length)])
    
    for i in truck_weights :
        while True :
            total_weight -= q[0]
            q.popleft()
            answer += 1
            if total_weight + i <= weight :
                q.append(i)
                total_weight += i
                break
            else :
                q.append(0)
    
    answer += len(q)
    return answer