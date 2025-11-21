def solution(participant, completion):
    answer = ''
    player = {}
    for i in participant :
        if i in player :
            player[i] += 1
        else :
            player[i] = 1
            
    for i in completion :
        player[i] -= 1
    
    for k, v in player.items() :
        if v != 0 :
            answer = k
            break
    
    return answer