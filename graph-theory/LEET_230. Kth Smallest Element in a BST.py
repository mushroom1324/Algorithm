# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        cur = root

        while True:
            while cur:
                stack.append(cur)
                cur = cur.left

            if not stack:
                break

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            cur = node.right


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        a = set()
        if not root:    return -1
        deq = collections.deque([(root)])
        while deq:
            cur = deq.popleft()
            a.add(cur.val)
            if cur.left:   deq.append((cur.left))
            if cur.right:  deq.append((cur.right))
        a = sorted(a)
        return a[k - 1]
"""