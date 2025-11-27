def time_change(x) :
    x += 10
    if x%100 >= 60 :
        x += 40
    return x

def solution(schedules, timelogs, startday):
    answer = 0
    people = len(schedules)
    for i in range(people) :
        tmp = time_change(schedules[i])
        for j in range(7) :
            day = (j-startday+1)%7
            if j != 5 and j != 6 :
                if tmp < timelogs[i][day] :
                    break
        else :
            answer += 1
    return answer