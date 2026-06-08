class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = len(position)
        stack = []
        temp = []
        i = 0
        while i < len(position):
            temp.append((position[i], speed[i]))
            i += 1
        
        temp.sort(reverse=True)

        stack.append((target - temp[0][0])/temp[0][1])
        j = 1
        while j < len(temp):
            if ((target - temp[j][0])/temp[j][1]) <= stack[-1]:
                fleet -= 1
            else:
                stack.append((target - temp[j][0])/temp[j][1])
            j += 1
        return fleet