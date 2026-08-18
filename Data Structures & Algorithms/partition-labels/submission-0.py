class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # count all chars
        count = defaultdict(int) # ch:count
        for ch in s:
            count[ch] += 1

        result = []
        onGoing = {}
        
        for each in s:
            if each in onGoing:
                onGoing[each] += 1
            else:
                onGoing[each] = 1

            done = True

            for ch in onGoing:
                if onGoing[ch] != count[ch]:
                    done = False

            if done:
                result.append(sum(list(onGoing.values())))
                onGoing = {}
        
        return result
