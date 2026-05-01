class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = []
        chk = set()
        for num in nums :
            chk.add(num)
        
        for i in range(l) :
            if i+1 not in chk :
                ans.append(i+1)
        return ans