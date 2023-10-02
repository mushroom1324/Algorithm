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
    
    private int ans;

    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;
        helper(root, 0);       
        return ans;
    }

    private void helper(TreeNode node, int val) {
        int cur = val * 10 + node.val;

        if (node.left == null && node.right == null) {
            ans += cur;
            return;
        }

        if (node.left != null) {
            helper(node.left, cur);
        }

        if (node.right != null) {
            helper(node.right, cur);
        }

    }
}
