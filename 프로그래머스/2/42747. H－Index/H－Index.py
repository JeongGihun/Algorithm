def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    num = 0
    for i in range(len(citations)):
        num += 1
        #print(citations[i], num, i)
        if citations[i] >= num and i+1 >= num :
            continue
        else :
            answer = num-1
            break
    else :
        answer = num
    return answer