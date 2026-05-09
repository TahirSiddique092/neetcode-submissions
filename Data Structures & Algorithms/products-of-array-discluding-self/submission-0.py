class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []
        prod = 1

        # calculating prefix product
        for num in nums:
            prefix.append(prod)
            prod *= num
        
        prod = 1
        # calculating postfix product
        for num in nums[::-1]:
            postfix.append(prod)
            prod *= num

        postfix.reverse()
        # calculating result
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])

        return result
        