from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = list(Counter(nums).items())
        l.sort(key=lambda x : x[1], reverse=True)
        ans = [x[0] for x in l]
        return ans[:k]