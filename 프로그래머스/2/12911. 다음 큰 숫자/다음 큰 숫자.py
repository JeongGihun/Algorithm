def solution(n):
    answer = 0
    check = bin(n)[2:].count("1")  # 2진수로 만들고 갯수를 확인한다
    
    while True :
        n += 1
        if bin(n)[2:].count("1") == check :
            ans = n
            break
        
    return ans