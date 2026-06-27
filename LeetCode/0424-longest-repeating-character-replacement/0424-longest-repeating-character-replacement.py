class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chk = dict()
        max_ = 1
        start, end = 0, 0
        # 존재하면 dict에 저장
        for i in range(len(s)) :
            chk[s[i]] = 0
        chk[s[0]] += 1

        # 본격적으로 확인
        for i in range(1, len(s)) :
            end += 1
            chk[s[end]] += 1
            while (end-start+1) - max(chk.values()) > k and start < end :
                chk[s[start]] -= 1
                start += 1
            max_ = max(max_, (end-start+1))
            
        return max_