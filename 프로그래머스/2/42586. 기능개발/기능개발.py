from collections import deque
import math
def solution(progresses, speeds):
    ans = []
    q = deque([])
    
    for i in range(len(speeds)) :
        tmp = math.ceil((100 - progresses[i]) / speeds[i])
        q.append(tmp)
    print(q)
    max_ = 0
    num = 0
    
    while q :
        tmp = q.popleft()
        num += 1
        if max_ == 0 :
            max_ = tmp
        if len(q) == 0 or max_ < q[0] :
            ans.append(num)
            num = 0
            max_ = 0
        
    
    return ans