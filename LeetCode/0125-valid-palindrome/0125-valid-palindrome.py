class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()
        chk = [x for x in l if 'a' <= x <= 'z' or '0' <= x <= '9']
        print(chk, chk[::-1])
        return True if chk == chk[::-1] else False
        