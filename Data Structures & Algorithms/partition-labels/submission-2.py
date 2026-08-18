class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        onGoing = {}
        ending = -1
        for idx, each in enumerate(s):
            if each in onGoing:
                onGoing[each] += 1
            else:
                onGoing[each] = 1
                ending = max(ending, s.rfind(each))

            if ending == idx:
                result.append(sum(list(onGoing.values())))
                onGoing = {}
                ending = -1
        
        return result
