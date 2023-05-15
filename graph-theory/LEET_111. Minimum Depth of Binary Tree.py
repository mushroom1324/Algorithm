# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        ans = 1e9
        deq = deque()

        deq.append((root, 1))

        while deq:
            cur, cnt = deq.popleft()

            if cur.left:
                deq.append((cur.left, cnt + 1))
            if cur.right:
                deq.append((cur.right, cnt + 1))
            if not cur.left and not cur.right:
                ans = min(ans, cnt)

        return ans

    
