# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1st: recursion
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node: Optional[TreeNode], lower_key: int, upper_key: int):

            if node:
                if lower_key < node.val < upper_key:
                    return helper(node.left, lower_key, node.val) and helper(node.right, node.val, upper_key)
                else:
                    return
            return True

        return helper(root, -1e11, 1e11)
"""


# 2nd: iteration
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        deq = deque()
        deq.append((root, -1e11, 1e11))

        while deq:
            node, lower, upper = deq.popleft()
            if node:
                if lower < node.val < upper:
                    deq.append((node.left, lower, node.val))
                    deq.append((node.right, node.val, upper))
                else:
                    return False
        return True


