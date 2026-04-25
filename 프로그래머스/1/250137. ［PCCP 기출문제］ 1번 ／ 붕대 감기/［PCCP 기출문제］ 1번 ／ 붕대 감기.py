def solution(bandage, health, attacks):
    ans = health
    for i in range(len(attacks)) :
        if i == 0 :
            ans -= attacks[i][1]
        else :
            time = attacks[i][0] - attacks[i-1][0] - 1
            ans += (time // bandage[0]) * bandage[2]
            ans += time * bandage[1]
            ans = ans if ans <= health else health
            ans -= attacks[i][1]
            
        if ans <= 0 :
                return -1
        
    
    return ans