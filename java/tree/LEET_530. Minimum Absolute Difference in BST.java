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

    private List<Integer> list = new ArrayList<>();

    public int getMinimumDifference(TreeNode root) {
        inOrder(root);
        int ans = 10000000;
        int prev = list.get(0);
        System.out.println(list.size());
        for(int i =1; i < list.size(); ++i) {
            ans = Math.min(ans, list.get(i) - prev);
            prev = list.get(i);
        }

        return ans;
    }

    public void inOrder(TreeNode node) {

        if (node != null) {
            inOrder(node.left);
            list.add(node.val);
            inOrder(node.right);
        }
    }
}