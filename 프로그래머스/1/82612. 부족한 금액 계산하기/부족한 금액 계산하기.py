def solution(price, money, count):
    for i in range(count) :
        money -= ((i+1) * price)
    if money >= 0 :
        answer = 0
    else :
        answer = (-1) * money
    return answer