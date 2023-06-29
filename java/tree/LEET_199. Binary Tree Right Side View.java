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
    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        Queue<TreeNode> level = new LinkedList<>();
        queue.add(root);
        List<Integer> ans = new ArrayList<>();

        while(queue.peek() != null) {
            TreeNode cur = queue.poll();


            if (cur.left != null) {
                level.add(cur.left);
            }
            if (cur.right != null) {
                level.add(cur.right);
            }

            if (queue.peek() == null) {
                ans.add(cur.val);
                queue = new LinkedList<>(level);
                level = new LinkedList<>();
            }
        }
        return ans;
    }
}