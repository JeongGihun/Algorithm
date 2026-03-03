import heapq

def solution(k, m, score):
    answer = 0
    score = list(map(lambda x : -x, score))
    heapq.heapify(score)
    num = len(score) // m
    
    for _ in range(num) :
        for i in range(m) :
            tmp = heapq.heappop(score)
        answer -= tmp * m
    
    return answer