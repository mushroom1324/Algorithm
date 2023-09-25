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
    
    private int sum;
    public TreeNode convertBST(TreeNode root) {

        helper(root);

        return root;        
    }

    public TreeNode helper(TreeNode node) {
        if (node == null) return null;

        helper(node.right);

        sum += node.val;

        node.val = sum;

        helper(node.left);

        return node;
    }
}
