class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers)-1
        while numbers[s] + numbers[e] != target :
            if numbers[s] + numbers[e] > target :
                e -= 1
            else :
                s += 1
        return [s+1, e+1]
            
