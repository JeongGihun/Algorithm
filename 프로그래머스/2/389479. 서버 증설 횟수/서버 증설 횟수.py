import math
def solution(players, m, k):
    answer = 0
    l = len(players)
    now = [m-1 for i in range(l)] # 최대 처리 가능한 인원
    for i in range(l) :
        if players[i] > now[i] :
            tmp = math.ceil((players[i]-now[i]) / m)
            answer += tmp
            for time in range(k) :
                if i+time < l :
                    now[i+time] += m * tmp       
    return answer