# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}

        def subTree(start: int, end: int) -> List[TreeNode]:
            if start > end:
                return [None]

            if (start, end) in dp:
                return dp[(start, end)]

            ans = []

            for i in range(start, end + 1):
                left_subtree = subTree(start, i - 1)
                right_subtree = subTree(i + 1, end)

                for left in left_subtree:
                    for right in right_subtree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)

            dp[(start, end)] = ans

            return ans

        return subTree(1, n)

