class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for num in nums :
            l.extend(list(str(num)))        
        return list(map(int, l))