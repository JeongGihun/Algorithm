import math
def solution(brown, yellow):
    sum_ = brown + yellow # 전체 합
    tmp = math.ceil(math.sqrt(sum_))
    b, l = tmp, tmp
    
    while True :
        check = b * l
        if check == sum_ and (b-2)*(l-2) == yellow :
            return [b, l]
        elif check > sum_ :
            l -= 1
        else :
            b += 1