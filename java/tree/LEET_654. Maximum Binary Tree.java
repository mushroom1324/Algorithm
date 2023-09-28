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

    private int[] nums;

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        this.nums = nums;

        return helper(0, nums.length - 1);
        
    }

    private TreeNode helper(int start, int end) {

            if (start > end) return null;

            int maxVal = -1;
            int index = 0;

            for (int i = start; i <= end; ++i) {
                if (nums[i] >= maxVal) {
                    maxVal = nums[i];
                    index = i;
                }
            }
            
            // given the index i which is indicates the max value..
            TreeNode root = new TreeNode(maxVal);

            root.left = helper(start, index - 1);
            root.right = helper(index + 1, end);

            return root;
    }
}
