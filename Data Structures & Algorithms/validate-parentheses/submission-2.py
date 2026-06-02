class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for c in s:
            if c in ['(', '{', '[']:
                temp.append(c)
            else:
                if (len(temp) > 0 ) and ((c == ')' and temp[-1] == '(') or (c == '}' and temp[-1] == '{') or (c == ']' and temp[-1] == '[')):
                    del temp[-1]
                else:
                    return False
        if len(temp) != 0:
            return False
        return True
        