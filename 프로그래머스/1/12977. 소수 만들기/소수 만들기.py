from itertools import combinations
import math
def solution(nums):
    ans = 0
    combi_list = list(combinations(nums, 3))
    sum_list = []
    for i in combi_list :
        sum_list.append(sum(i))
    
    
    for i in sum_list :
        for j in range(2, math.ceil(i**0.5)+1) :
            if i % j == 0 :
                break
        else :
            ans += 1
    

    return ans