def solution(x, y, n):
    answer = 0
    stack = [y]
    while stack :
        tmp = []
        if x in stack :
            break
        answer += 1
        for i in stack :
            if i % 2 == 0 :
                tmp.append(i//2)
            if i % 3 == 0 :
                tmp.append(i//3)
            if i-n >= x :
                tmp.append(i-n)
        stack = tmp
    else :
        answer = -1
    return answer