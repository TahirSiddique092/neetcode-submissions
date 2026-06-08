class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                rem = stack.pop()[1]
                output[rem] = i - rem
            stack.append((t, i))
        return output
                
