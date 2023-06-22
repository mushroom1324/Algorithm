/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int i = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, inorder, 0, preorder.length-1);
    }

    public TreeNode helper(int[] preorder, int[] inorder, int left, int right) {
        // base case
        if(i == preorder.length || left > right) return null;

        TreeNode root = new TreeNode(preorder[i]);
        int j = left;
        while(j <= right && preorder[i] != inorder[j]) j++;
        i++;
        root.left = helper(preorder, inorder, left, j - 1);
        root.right = helper(preorder, inorder, j + 1, right);
        return root;
    }
}