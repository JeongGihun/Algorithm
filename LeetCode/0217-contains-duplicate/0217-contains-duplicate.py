class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        flag = False
        for num in nums :
            if num in s :
                flag = True
            s.add(num)
        return flag