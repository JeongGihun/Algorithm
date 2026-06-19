class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        ans = [0]
        for i in range(len(s)) :
            while s[i] in s[start:end] :
                start += 1
            end += 1
            ans.append(end-start)
        return max(ans)
            