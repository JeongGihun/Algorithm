import string
from collections import deque

def solution(msg):
    answer = []
    # A~Z부터 만들어주기
    s = {c:idx+1 for idx, c in enumerate(string.ascii_uppercase)}
    num = 26
    q = deque(msg)
    tmp = ''
    while q :
        tmp += q.popleft()
        if tmp not in s :
            num += 1
            s[tmp] = num
            answer.append(s[tmp[:-1]])
            tmp = tmp[-1]
    answer.append(s[tmp])
    return answer