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

    public int longestUnivaluePath(TreeNode root) {
        
        calculate(root, -1001);
        return ans;
    }

    private int calculate(TreeNode node, int val) {
        if (node == null) return 0;
    
        int left = 0, right = 0;

        if (node.left != null) left = calculate(node.left, node.val);
        if (node.right != null) right = calculate(node.right, node.val);

        ans = Math.max(ans, left + right);

        // if value is not univalue
        if (node.val != val) return 0;
        // if value is univalue
        else return Math.max(left, right) + 1;
    }
}
