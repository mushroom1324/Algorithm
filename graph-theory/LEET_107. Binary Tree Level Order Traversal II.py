# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        deq = deque()
        temp = deque()

        deq.append(root)

        ans = []

        while deq:

            while deq:
                temp.append(deq.popleft())

            each = []
            while temp:
                cur = temp.popleft()

                each.append(cur.val)

                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)

            ans.append(each)

        return reversed(ans)
