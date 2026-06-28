# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # A node is valid if it lies bewteen lower bound and upper bound
        # If a tree grows to left, update its upper bound
        # If a tree grows to right, update its lower bound
        if not root:
            return True
        
        return self.isValid(root, float('-inf'), float('inf'))
        
    def isValid(self, node, lower, upper):
        if not node:
            return True
        
        if not (node.val > lower) or not (node.val < upper):
            return False
        
        return self.isValid(node.left, lower, node.val) and self.isValid(node.right, node.val, upper)
        

        