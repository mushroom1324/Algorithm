# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deq = deque()
        deq.append((p, q))

        while deq:

            cur_p, cur_q = deq.popleft()

            if not cur_p and not cur_q:
                continue
            elif not cur_p or not cur_q:
                return False
            else:
                if cur_p.val != cur_q.val:
                    return False
                deq.append((cur_p.left, cur_q.left))
                deq.append((cur_p.right, cur_q.right))
        return True
