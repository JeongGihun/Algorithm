import re

def solution(new_id):
    answer = ''
    tmp = list(new_id.lower()) #1
    for i in tmp : #2
        if 'a' <= i <= 'z' or i in list('-_.') or '0' <= i <= '9' :
            answer += i
    answer = re.sub(r'\.+', '.', answer)
    if answer and answer[0] == '.' :
        answer = answer[1:]
    if answer and answer[-1] == '.' :
        answer = answer[:len(answer)-1]
    if answer == "" : 
        answer = 'a'
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:len(answer)-1]
    if len(answer) <= 2 :
        answer += answer[-1] * (3-len(answer))
    return answer