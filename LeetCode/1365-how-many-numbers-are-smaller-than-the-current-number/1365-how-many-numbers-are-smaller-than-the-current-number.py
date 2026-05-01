class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        for i in range(l) :
            chk = 0
            for j in range(l) :
                if i != j :
                    chk += 1 if nums[i] > nums[j] else 0
            ans.append(chk)
        return ans