from collections import Counter
def solution(N, stages):
    people = Counter(stages)
    n = len(stages)
    probability = []
    
    for i in range(N) :
        if n != 0 :
            tmp = people[i+1] / n
            n -= people[i+1]
            probability.append([tmp, i+1])
        else :
            probability.append([0.0, i+1])
    print(probability)
    probability.sort(key = lambda x : x[0], reverse= True)
    ans = list(map(lambda x : x[1], probability))
    
    return ans