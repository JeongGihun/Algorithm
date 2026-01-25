from collections import deque
def solution(n, m, section):
    ans = 0
    q = deque(section)
    
    while q :
        ans += 1
        tmp = q[0] + m - 1
        while q :
            if tmp >= q[0] :
                q.popleft()
            else : 
                break
    
    return ans