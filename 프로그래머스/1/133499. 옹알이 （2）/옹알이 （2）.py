def solution(babbling):
    answer = 0
    dic = {"aya", "ye", "woo", "ma"}
    for i in babbling :
        before = ''
        while True :
            for j in range(1, len(i)+1) :
                if i[:j] in dic and i[:j] != before :
                    before = i[:j]
                    i = i[j:]
                    break
            else :
                break
                
        if i == "" :
            answer += 1
                
    return answer