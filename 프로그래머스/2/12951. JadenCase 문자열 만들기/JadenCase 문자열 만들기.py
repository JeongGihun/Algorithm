def solution(s):
    s = s.lower()
    ans = []
    print(s)
    for i in range(len(s)) :
        if i == 0 :
            tmp = s[i].upper()
        elif i > 0 and s[i-1] == " " :
            tmp = s[i].upper()
        else :
            tmp = s[i]
        ans.append(tmp)
    
    return ''.join(ans)