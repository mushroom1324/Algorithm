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
    private int low, high;
    private TreeNode ans = new TreeNode();

    public TreeNode trimBST(TreeNode root, int low, int high) {
        this.low = low;
        this.high = high;

        return helper(root);
        
    }

    private TreeNode helper(TreeNode node) {
        if (node == null) return null;

        if (checkLow(node.val)) {
            return helper(node.right);
        }
        else if (checkHigh(node.val)) {
            return helper(node.left);
        }
        else {
            node.left = helper(node.left);
            node.right = helper(node.right);
            return node;
        }

    }

    private boolean checkLow(int val) {
        if (val < low) return true;
        return false;
    }

    private boolean checkHigh(int val) {
        if (val > high) return true;
        return false;
    }
}
