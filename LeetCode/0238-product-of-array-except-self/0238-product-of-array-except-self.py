class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1 for i in range(l)]

        for i in range(1, l) :
            ans[i] = ans[i-1] * nums[i-1]
        chk = 1
        for i in range(l-2, -1, -1) :
            chk *= nums[i+1]
            ans[i] = ans[i] * chk
        
        return ans