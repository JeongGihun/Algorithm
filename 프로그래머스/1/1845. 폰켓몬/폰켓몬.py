def solution(nums):
    answer = 0
    pocket = set()
    
    for i in nums :
        pocket.add(i)
    num = len(nums) // 2
    answer = min(len(pocket), num)
    
    return answer