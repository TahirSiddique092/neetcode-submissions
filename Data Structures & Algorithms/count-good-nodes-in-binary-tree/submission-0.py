# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.nodeCount = 0

    def goodNodes(self, root: TreeNode) -> int:
        # any node to be good, should be greater than root node 
        # any node to be good, should be greater than other nodes in the path.
        # so if a node knows that my highest node in this path is less than or equal to me then it is a good node.

        if not root:
            return []

        self.goodRecursive(root, root.val)

        return self.nodeCount

    def goodRecursive(self, node, highest):
        if not node:
            return None
        
        if node.val >= highest:
            self.nodeCount += 1
            highest = node.val
        
        self.goodRecursive(node.left, highest)
        self.goodRecursive(node.right, highest)
        