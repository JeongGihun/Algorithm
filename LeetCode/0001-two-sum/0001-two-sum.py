class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)) :
            if nums[i-1] + nums[i] == target : 
                return [i-1, i]
        