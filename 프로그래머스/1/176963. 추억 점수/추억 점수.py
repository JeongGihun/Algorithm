def solution(name, yearning, photo):
    answer = []
    check = {name[i]:yearning[i] for i in range(len(name))}
    
    for num in range(len(photo)) :
        score = 0 
        for people in photo[num] :
            if people in check :
                score += check[people]
        answer.append(score)
    
    return answer