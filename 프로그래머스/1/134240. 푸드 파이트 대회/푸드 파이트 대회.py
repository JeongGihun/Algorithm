from collections import deque
def solution(food):
    q = deque([0])
    ans = ''
    for i in range(len(food)-1,0,-1) :
        num = food[i]//2
        q.append(num * str(i))
        q.appendleft(num * str(i))
    
    while q :
        ans += str(q.popleft())
    return ans