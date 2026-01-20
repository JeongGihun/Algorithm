def solution(n, arr1, arr2):
    answer = []
    graph = [] * n
    
    for i in range(n) :
        tmp = int(arr1[i] | arr2[i])
        tmp = bin(tmp)[2:]
        tmp2 = ''
        for j in tmp :
            if j == '1' :
                tmp2 += '#'
            else :
                tmp2 += ' '
        if len(tmp2) != n :
            tmp2 = ' ' * (n-len(tmp2)) + tmp2
        answer.append(tmp2)
    
    
    return answer