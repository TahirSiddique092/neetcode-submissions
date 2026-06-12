class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for each in matrix:
            if target <= each[-1]:
                left = 0
                right = len(each)-1
                while left <= right:
                    mid = left + (right - left)//2
                    if each[mid] == target:
                        return True
                    elif each[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
        