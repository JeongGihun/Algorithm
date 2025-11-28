class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        check_num = 0
        for i in nums :
            if i==1 :
                check_num += 1
            else :
                max_num = max(max_num, check_num)
                check_num = 0
        if check_num > 0:
            max_num = max(max_num, check_num)
        return max_num