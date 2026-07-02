# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        self.i = 0

    def preorder(self, root) -> str:
        if not root:
            return "N"

        s = ",".join([str(root.val), self.preorder(root.left), self.preorder(root.right)])
        return s

    def convert(self, data):
        token = data[self.i]
        self.i += 1

        if token == "N":
            return None

        node = TreeNode(int(token))
        node.left = self.convert(data)
        node.right = self.convert(data)

        return node

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        return self.convert(data.split(","))
         

