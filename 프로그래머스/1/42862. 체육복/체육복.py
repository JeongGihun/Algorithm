def solution(n, lost, reserve):
    answer = 0
    l = set(lost)
    r = set(reserve)
    l, r = l - r, r - l
    
    for tmp in r:
        if tmp-1 in l :
            l.remove(tmp-1)
            continue
        if tmp+1 in l :
            l.remove(tmp+1)
            continue
    
    return n-len(l)