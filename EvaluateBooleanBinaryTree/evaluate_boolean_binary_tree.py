class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        # If the node is a leaf node
        if root.left is None and root.right is None:
            return bool(root.val)

        # Recursively evaluate the left and right children
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        # Apply the operation based on the value of the current node
        if root.val == 2:  # OR operation
            return left_val or right_val
        elif root.val == 3:  # AND operation
            return left_val and right_val
