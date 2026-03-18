from collections import Counter

def solution(weights):
    ans = 0
    l = Counter(weights)
    check = [(2, 3), (1, 2), (3, 4)]
    for i in l.keys() :
        for c in check :
            if i % c[0] == 0 :
                tmp = ((i//c[0]) * c[1])
            else :
                continue

            if tmp in l.keys() and i < tmp :
                ans += l[i] * l[tmp]
                
    for i in l.keys() :
        if l[i] >= 2 :
            ans += l[i] * (l[i]-1) // 2
    return ans