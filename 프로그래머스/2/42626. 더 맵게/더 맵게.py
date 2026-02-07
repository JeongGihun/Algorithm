import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    check = 0
    
    while len(scoville) > 1 and scoville[0] < K :
        answer += 1
        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        check = tmp1+tmp2*2
        heapq.heappush(scoville, check)
    
    return answer if scoville[0] >= K else -1