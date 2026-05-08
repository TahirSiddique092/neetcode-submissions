class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for each in strs:
            count = [0] * 26
            for ch in each:
                count[ord(ch) - ord('a')] += 1

            result[tuple(count)].append(each)
        
        return list(result.values())
            
        