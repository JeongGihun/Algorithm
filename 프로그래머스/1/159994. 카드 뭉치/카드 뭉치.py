from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    q1 = deque(cards1)
    q2 = deque(cards2)
    ans_q = deque(goal)
    while ans_q :
        if q1 and ans_q[0] == q1[0] :
            ans_q.popleft()
            q1.popleft()
        elif q2 and ans_q[0] == q2[0] :
            ans_q.popleft()
            q2.popleft()
        else :
            break
            
    if not ans_q :
        answer = "Yes"
    else:
        answer = "No"
    
    return answer