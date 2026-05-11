class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for alphabet in s :
            if alphabet not in d :
                d[alphabet] = 0
            d[alphabet] += 1
        
        d2 = dict()
        for alphabet in t :
            if alphabet not in d2 :
                d2[alphabet] = 0
            d2[alphabet] += 1

        if d == d2 :
            return True
        else :
            return False
        