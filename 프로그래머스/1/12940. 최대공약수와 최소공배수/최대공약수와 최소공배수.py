def solution(n, m):
    answer = []
    num = 0
    for i in range(n+1) :
        if n % (i+1) == 0 and m % (i+1) == 0:
            num = i+1
    answer.append(num) # 최소공배수
    n /= num
    m /= num
    answer.append(num*n*m)
    
    return answer