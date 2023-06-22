/**

    시간100 메모리52

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
    void postOrderSwap(TreeNode cur) {
        if (cur == null) return;

        postOrderSwap(cur.left);
        postOrderSwap(cur.right);

        TreeNode temp = cur.left;
        cur.left = cur.right;
        cur.right = temp;

    }
    public TreeNode invertTree(TreeNode root) {

        postOrderSwap(root);
        return root;
    }
}