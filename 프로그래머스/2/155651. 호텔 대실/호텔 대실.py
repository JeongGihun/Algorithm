def solution(book_time):
    ans = 0
    check = 0
    l = [] # in, out 및 시간(그냥 분으로 전부 표기)
    for t in book_time :
        s, e = t[0], t[1]
        l.append([int(t[0][:2]) * 60 + int(t[0][3:]) ,"in"])
        l.append([int(t[1][:2]) * 60 + int(t[1][3:]) + 9 ,"out"])
    l.sort()
    for i in l :
        if i[1] == "in" :
            check += 1
        else :
            check -= 1
        ans = max(ans, check)
    
    return ans