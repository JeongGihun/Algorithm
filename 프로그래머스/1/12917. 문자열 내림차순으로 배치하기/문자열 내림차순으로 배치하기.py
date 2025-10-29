def solution(s):
    l = []
    sen = ''
    for i in s :
        l.append(ord(i))
    l.sort(reverse=True)
    
    for i in l :
        sen += chr(i)
    return sen