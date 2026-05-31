class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lstr = ""
        maxl = 0
        for i in range(len(s)):
            if s[i] not in lstr:
                lstr += s[i]
            else:
                maxl = max(maxl, len(lstr))
                lstr = lstr[lstr.find(s[i])+1:] + s[i]
        maxl = max(maxl, len(lstr))
        return maxl