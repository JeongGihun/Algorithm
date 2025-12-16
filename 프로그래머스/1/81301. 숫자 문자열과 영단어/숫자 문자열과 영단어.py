from collections import deque
def solution(s):
    num = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4",
        "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    l = deque(list(s))
    tmp = ''
    ans = ''
    while l :
        tmp += l.popleft()
        if "0" <= tmp <= "9" :
            ans += tmp
            tmp = ''
        elif tmp in num :
            ans += num[tmp]
            tmp = ''
        
    return int(ans)