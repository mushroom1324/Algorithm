# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tree = []

        def inorder(node):
            if node:
                inorder(node.left)
                tree.append(node)
                inorder(node.right)

        inorder(root)
        wrong = []
        for i in range(1, len(tree)):
            if tree[i - 1].val > tree[i].val:
                wrong.append(i - 1)

        if len(wrong) == 1:
            tree[wrong[0] + 1].val, tree[wrong[0]].val = tree[wrong[0]].val, tree[wrong[0] + 1].val
        else:
            tree[wrong[1] + 1].val, tree[wrong[0]].val = tree[wrong[0]].val, tree[wrong[1] + 1].val
