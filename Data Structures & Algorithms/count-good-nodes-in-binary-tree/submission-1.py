# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # any node to be good, should be greater than root node 
        # any node to be good, should be greater than other nodes in the path.
        # so if a node knows that my highest node in this path is less than or equal to me then it is a good node.

        if not root:
            return 0

        return self.goodRecursive(root, root.val)

    def goodRecursive(self, node, highest):
        if not node:
            return 0
        
        count = 0
        if node.val >= highest:
            count += 1
            highest = node.val
        
        count += self.goodRecursive(node.left, highest) 
        count += self.goodRecursive(node.right, highest)

        return count
        