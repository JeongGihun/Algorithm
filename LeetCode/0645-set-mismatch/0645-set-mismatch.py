class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        tmp = 0
        for i in nums :
            if i in s :
                tmp = i
            else :
                s.add(i)
        # 2, 3
        for i in range(len(nums)) :
            if i+1 not in s :
                return [tmp, i+1] 