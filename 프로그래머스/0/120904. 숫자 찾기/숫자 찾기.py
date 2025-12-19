def solution(num, k):
    tmp = str(num)
    answer = tmp.find(str(k)) 
    if answer != -1 :
        answer +=1

    return answer