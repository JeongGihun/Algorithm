def solution(a, b):
    answer = ''
    day_ = 0
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(a-1) :
        day_ += mon[i]
    day_ += b
    day_ %= 7
    check_day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    return check_day[day_-1]