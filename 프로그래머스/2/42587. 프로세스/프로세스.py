from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    
    while q :
        max_num = max(q)
        
        if max_num == q[0] :
            q.popleft()
            answer += 1
            if location == 0 :
                break
        else :
            q.rotate(-1)
        location -= 1
        
        if location < 0 :
            location += len(q)
        
    
    return answer