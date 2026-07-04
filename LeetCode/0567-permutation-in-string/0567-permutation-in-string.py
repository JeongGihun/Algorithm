import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {x:0 for x in string.ascii_lowercase}
        for i in s1 :
            d[i] -= 1
        
        # if s1 in permutation s2 -> same length
        for i in s2[:len(s1)] :
            d[i] += 1

        if (all(v==0 for v in d.values())) :
            return True
        # 8, 2, 7
        for i in range(len(s2)-len(s1)) :
            d[s2[i+len(s1)]] += 1
            d[s2[i]] -= 1
            if (all(v==0 for v in d.values())) :
                return True
        else :
            return False