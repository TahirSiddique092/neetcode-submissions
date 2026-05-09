class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += word + "π"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        l = ""
        result = []
        while i < len(s):
            if s[i] != "π":
                l += s[i]
            else:
                result.append(l)
                l = ""
            i += 1
        return result



