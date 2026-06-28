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
            node = curr.popleft()
            if node:
                if node.left: 
                    nxt.append(node.left)
                if node.right: 
                    nxt.append(node.right)
                if len(curr) == 0:
                    result.append(node.val)
                    curr = nxt
                    nxt = collections.deque()
        
        return result
