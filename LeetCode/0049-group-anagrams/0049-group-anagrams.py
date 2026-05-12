from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        idx = 0
        for str in strs :
            tmp = tuple(sorted(Counter(str).items()))
            if tmp not in ans :
                ans[tmp] = []
            ans[tmp].append(str)

        return list(ans.values())
        