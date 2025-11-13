def solution(people, limit):
    people.sort()
    answer = 0
    s, e = 0, len(people)-1 # 슬라이스 윈도우 값 초기화
    
    while True :
        if s > e :
            break   
        
        if s == e :
            answer += 1
            s += 1
        elif people[s] + people[e] > limit :
            answer += 1
            e -= 1
        else :
            answer += 1
            s += 1
            e -= 1 
    
    return answer