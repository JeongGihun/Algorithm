def solution(clothes):
    dic = {}
    answer = 1
    for i in range(len(clothes)) :
        if clothes[i][1] not in dic :
            dic[clothes[i][1]] =[]
        dic[clothes[i][1]].append(clothes[i][0])

    
    for k,v in dic.items() :
        answer *= (len(v)+1)
    answer -= 1
    return answer