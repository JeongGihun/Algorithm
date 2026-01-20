def solution(answers):
    answer = []
    o = [0, 0, 0]
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    l1, l2, l3 = len(su1), len(su2), len(su3)
    for i in range(len(answers)) :
        if answers[i] == su1[i%l1] :
            o[0] += 1
        if answers[i] == su2[i%l2] :
            o[1] += 1
        if answers[i] == su3[i%l3] :
            o[2] += 1 
    
    for i in range(3) :
        if max(o) == o[i] :
            answer.append(i+1)
    
    return answer