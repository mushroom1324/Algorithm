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
    public int maxLevelSum(TreeNode root) {

        return bfs(root);
        
    }

    private int bfs(TreeNode root) {

        int result = 1;
        int maxVal = -1000000;
        
        int level = 1;

        int children = 1;
        int nextChildren = 0;
        int sum = 0;

        Deque<TreeNode> q = new ArrayDeque<>();

        q.add(root);

        while (!q.isEmpty()) {
            
            TreeNode cur = q.poll();

            sum += cur.val;

            if (cur.left != null) {
                ++nextChildren;
                q.add(cur.left);
            }
            if (cur.right != null) {
                ++nextChildren;
                q.add(cur.right);
            }

            if (--children == 0) {
                if (sum > maxVal) {
                    maxVal = sum;
                    result = level;
                }
                ++level;
                sum = 0;
                children = nextChildren;
                nextChildren = 0;
            }

        }

        return result;

    }
}
