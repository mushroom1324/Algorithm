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

    private int cnt;

    public int pathSum(TreeNode root, int targetSum) {

        if (root == null) return 0;

        helper(root, targetSum, 0l);
        pathSum(root.left, targetSum);
        pathSum(root.right, targetSum);

        return cnt;
        
    }

    private void helper(TreeNode node, int targetSum, long currentSum) {
        if (node == null) return;
        
        currentSum += node.val;

        if (currentSum == targetSum) ++cnt;

        helper(node.left, targetSum, currentSum);
        helper(node.right, targetSum, currentSum);
    }
}
