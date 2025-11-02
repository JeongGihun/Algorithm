def solution(n):
    answer = 0
    l = [1, 2]
    
    while len(l) != n :
        l.append((l[-2]+l[-1])%1000000007)
    return l[-1]