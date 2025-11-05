def solution(n):

    l = [0 for i in range(n+1)]
    l[1] = 1
    if n < 2 :
        return n
    
    for i in range(2, n+1) :
        l[i] = (l[i-1] + l[i-2]) % 1234567
        # (2, 3) -> l[2] = l[1] + l[0]
        # (2, 3) -> l[3] = l[2] + l[1]
            
    return l[-1]
    
    
    return answer