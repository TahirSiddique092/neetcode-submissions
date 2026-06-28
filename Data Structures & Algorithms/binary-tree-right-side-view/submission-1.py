# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # add elements in a queue at each level
        # pop all elements and store the last one and add their childern
        if not root:
            return []
        
        curr = collections.deque()
        nxt = collections.deque()
        result = []
        curr.append(root)

        while curr:
            for _ in range(len(curr)):
                node = curr.popleft()
                if node:
                    if node.left: 
                        curr.append(node.left)
                    if node.right: 
                        curr.append(node.right)
            result.append(node.val)
        
        return result
