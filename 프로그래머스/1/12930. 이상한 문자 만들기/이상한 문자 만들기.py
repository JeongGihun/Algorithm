def solution(s):
    answer = ''
    check = 0
    for word in s :
        if word == ' ' :
            answer += ' '
            check = 0
        else :
            if check % 2 == 0 :
                answer += word.upper()
            else :
                answer += word.lower()
            check += 1
    
    return answer