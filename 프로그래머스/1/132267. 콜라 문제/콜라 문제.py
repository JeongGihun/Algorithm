def solution(a, b, n):
    answer = 0
    while n//a >= 1 :
        tmp = n//a # 몇 세트 줄 것인지
        n %= a # 주고 남은것
        answer += tmp * b
        n += tmp * b         #print(n, answer)
    return answer