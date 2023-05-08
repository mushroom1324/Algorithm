# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        stack = deque()
        temp = deque()
        temp.append(root)
        ans = []

        rev = True
        while temp:
            temp.reverse()
            stack = temp
            temp = deque()
            ans_temp = []
            print(stack)
            while stack:
                cur = stack.popleft()
                print(cur.val)

                ans_temp.append(cur.val)
                if rev:
                    if cur.left:
                        temp.append(cur.left)
                    if cur.right:
                        temp.append(cur.right)
                else:
                    if cur.right:
                        temp.append(cur.right)
                    if cur.left:
                        temp.append(cur.left)
            rev = not rev
            if ans_temp:
                ans.append(ans_temp)
        return ans

