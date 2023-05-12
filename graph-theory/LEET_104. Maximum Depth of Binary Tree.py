# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        deq = deque()
        deq.append((root, 1))
        ans = 0

        while deq:
            cur, cnt = deq.popleft()

            ans = max(ans, cnt)

            if cur.left:
                deq.append((cur.left, cnt + 1))
            if cur.right:
                deq.append((cur.right, cnt + 1))

        return ans