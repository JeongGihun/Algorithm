def solution(s):
    ans = []
    s = s[1:-1]
    l = s.split('},{')
    l[0] = l[0][1:]
    l[-1] = l[-1][:-1]
    
    stack = []
    for i in l :
        tmp = i.split(',')
        stack.append(tmp)
    stack.sort(key=len)
    
    for i in stack :
        for j in i :
            if int(j) not in ans :
                ans.append(int(j))
                break
    return ans