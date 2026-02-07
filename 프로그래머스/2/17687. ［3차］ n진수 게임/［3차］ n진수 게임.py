def solution(n, t, m, p):
    answer = ''
    stack = [0]
    num = 1
    while len(stack) <= (t-1) * m +p :
        tmp = []
        tmp_num = num
        while tmp_num != 0 :
            tmp.append(tmp_num%n)
            tmp_num //= n
        num += 1
        tmp.reverse()
        stack.extend(tmp)
        #print(stack)
    
    for i in range(p-1, (t-1) * m +p+ 1, m) :
        if 10 <= stack[i] < 16 :
            answer += chr(stack[i]+55)
        else :
            answer += str(stack[i])
    
    return answer