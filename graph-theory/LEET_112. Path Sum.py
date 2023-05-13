# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        deq = deque()
        ans = 0
        deq.append((root, root.val))

        while deq:
            cur, cnt = deq.popleft()
            if not cur.left and not cur.right and cnt == targetSum:
                return True
            if cur.left:
                deq.append((cur.left, cnt + cur.left.val))
            if cur.right:
                deq.append((cur.right, cnt + cur.right.val))

        return False