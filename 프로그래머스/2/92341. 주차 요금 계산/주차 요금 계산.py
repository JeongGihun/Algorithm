import math
def solution(fees, records):
    answer = []
    # 필요한 값 : 입차 시간, 누적 시간
    car = {}
    
    for i in records :
        tmp = i.split()
        if tmp[2] == 'IN' :
            if tmp[1] not in car :
                car[tmp[1]] = [tmp[0]]
            else :
                car[tmp[1]].append(tmp[0])
        if tmp[2] == 'OUT' :
            car[tmp[1]].append(tmp[0])
    
    for i in car :
        if len(car[i]) % 2 == 1 :
            car[i].append('23:59')
    # 정산 마무리 해주기
    
    for num in sorted(car) :
        time = 0
        while car[num] :
            o_time = car[num].pop()
            i_time = car[num].pop()
            h = int(o_time[:2]) - int(i_time[:2])
            m = int(o_time[3:]) - int(i_time[3:])
            time += 60 * h + m
        money = fees[1]
        if math.ceil((time-fees[0]) / fees[2]) >= 0 :
            money += math.ceil((time-fees[0]) / fees[2]) * fees[3]
        answer.append(money)
    
    return answer