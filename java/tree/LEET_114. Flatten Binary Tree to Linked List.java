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
    private List<TreeNode> list = new ArrayList<>();

    public void flatten(TreeNode root) {

        TreeNode temp = root;

        if (temp == null) return;

        helper(root);

        for (int i = 1; i < list.size(); ++i) {
            temp.left = null;
            temp.right = list.get(i);
            temp = temp.right;
        }

    }

    private void helper(TreeNode node) {
        list.add(node);
        if (node.left != null) helper(node.left);
        if (node.right != null) helper(node.right);
    }

}