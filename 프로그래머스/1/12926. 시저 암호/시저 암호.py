def solution(s, n):
    answer = ''
    for word in s :
        tmp = ord(word)
        if 65 <= tmp < 91 :
            tmp = tmp+n if tmp+n < 91 else tmp+n-26 
        if 97 <= tmp < 123 :
            tmp = tmp+n if tmp+n < 123 else tmp+n-26 
        answer += chr(tmp)
    
    return answer