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
    public int averageOfSubtree(TreeNode root) {
        int[] result = new int[1];
        traverse(root, result);
        return result[0];
        
    }

    private int[] traverse(TreeNode node, int[] result) {
        if (node == null) return new int[] {0, 0};

        int[] left = traverse(node.left, result);
        int[] right = traverse(node.right, result);

        int curSum = node.val + left[0] + right[0];
        int curCnt = 1 + left[1] + right[1];

        if (curSum / curCnt == node.val) result[0]++;

        return new int[] {curSum, curCnt};
    }
}
