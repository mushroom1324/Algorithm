# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left = []
        right = []

        def left_traverse(node):
            if not node:
                left.append(-1)
                return

            left.append(node.val)
            left_traverse(node.left)
            left_traverse(node.right)

        def right_traverse(node):
            if not node:
                right.append(-1)
                return

            right.append(node.val)
            right_traverse(node.right)
            right_traverse(node.left)

        left_traverse(root.left)
        right_traverse(root.right)

        print(left)
        print(right)

        if len(left) != len(right):
            return False

        for i in range(len(left)):
            if left[i] != right[i]:
                return False
        return True

