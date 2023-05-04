# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        deq = deque()
        ans = []
        level = [1, 0]
        temp = []
        i = 0

        deq.append(root)

        while deq:
            cur = deq.popleft()
            temp.append(cur.val)
            level[i] -= 1

            if cur.left:
                level[i + 1] += 1
                deq.append(cur.left)
            if cur.right:
                level[i + 1] += 1
                deq.append(cur.right)

            if level[i] == 0:
                ans.append(temp)
                temp = list()
                i += 1
                level.append(0)

        return ans
