def time_change(x) :
    x += 10
    if x%100 >= 60 :
        x += 40
    return x

def To_monday(x, startday) :
    return (x-startday+1)%7

def solution(schedules, timelogs, startday):
    answer = 0
    people = len(schedules)
    for i in range(people) :
        tmp = time_change(schedules[i])
        for j in range(7) :
            day = To_monday(j, startday)
            if j != 5 and j != 6 :
                if tmp < timelogs[i][day] :
                    break
        else :
            answer += 1
    return answer