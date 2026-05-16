class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = [0]
        s = set(nums)
        for num in s :
            tmp = 1
            if num-1 in s :
                continue
            while num+1 in s :
                tmp += 1
                num += 1
            ans.append(tmp)
        return max(ans)