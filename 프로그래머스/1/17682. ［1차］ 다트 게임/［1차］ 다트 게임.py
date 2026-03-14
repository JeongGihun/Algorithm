def solution(dartResult):
    ans = []
    tmp = ''
    l = []
    for i in dartResult :
        tmp += i
        if i == "#" or i == "*" :
            l.append(i)
            tmp = ''
        if 'A' <= i <= 'Z' :
            l.append(tmp)
            tmp = ''
    
    for i in l :
        if len(i) > 1 :
            if i[-1] == "S" :
                ans.append(pow(int(i[:-1]), 1))
            if i[-1] == "D" :
                ans.append(pow(int(i[:-1]), 2))
            if i[-1] == "T" :
                ans.append(pow(int(i[:-1]), 3))
        if i == "#" :
            ans[-1] = (-1) * ans[-1]
        if i == "*" :
            ans[-1] *= 2
            if len(ans) > 1 :
                ans[-2] *= 2
    
    
    return sum(ans)