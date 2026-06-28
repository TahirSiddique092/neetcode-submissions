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
        
        queue = collections.deque()
        result = []
        queue.append(root)

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    if node.left: 
                        queue.append(node.left)
                    if node.right: 
                        queue.append(node.right)
            result.append(node.val)
        
        return result
