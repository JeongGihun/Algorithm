def solution(n):
    answer = 0
    sieve = [True for i in range(n+1)]
    sieve[0] = False
    sieve[1] = False
    for i in range(n) :
        if sieve[i] == False :
            continue
        else :
            for j in range(2, n//i+1) :
                sieve[i*j] = False
    
    
    return sieve.count(True)