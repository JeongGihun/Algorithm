class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l = len(nums)
        nums.sort()
        ans = []
        for i in range(l) :
            s, e = i+1, l-1
            if i > 0 and nums[i] == nums[i-1] :
                continue
            while s < e :
                if nums[i]+nums[s]+nums[e] == 0 :
                    if s > 0 and e < l-1 and nums[s] == nums[s-1] and nums[e] == nums[e+1] :
                        s += 1
                    else :
                        tmp = [nums[i], nums[s], nums[e]]
                        ans.append(tmp)
                        s += 1
                        e -= 1
                if nums[i]+nums[s]+nums[e] > 0 :
                    e -= 1
                elif nums[i]+nums[s]+nums[e] < 0 :
                    s += 1
                
        return ans