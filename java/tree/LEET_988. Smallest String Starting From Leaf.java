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

    String ans = "";

    public String smallestFromLeaf(TreeNode root) {
        dfs(root, "");
        return ans;    
    }

    private void dfs(TreeNode node, String str) {
        if (node == null) return;
        char c = (char)('a' + node.val);

        if (node.left == null && node.right == null) {
            String s = new StringBuilder(str + c).reverse().toString();
            if (ans == "") ans = s;
            else if (ans.compareTo(s) > 0) ans = s;
        }
        else {
            dfs(node.left, str + c);
            dfs(node.right, str + c);
        }
    }
}
