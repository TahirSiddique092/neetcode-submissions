class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        for ch in s1:
            s1_freq[ch] += 1
        i=0
        while (i+len(s1)) <= len(s2) :
            sub_freq = defaultdict(int)
            for ch in s2[i:i+len(s1)]:
                sub_freq[ch] += 1 
            
            if sub_freq == s1_freq :
                return True
            i += 1
        return False


        