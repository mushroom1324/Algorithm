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
class Pair {
    public TreeNode node;
    public int level;

    Pair(TreeNode node, int level) {
        this.node = node;
        this.level = level;
    }
}
class Solution {

    private Queue<Pair> queue = new LinkedList<>();
    private int maxLevel = -1;
    private int ans;

    public int findBottomLeftValue(TreeNode root) {
        
        bfs(root);
        return ans;

    }

    private void bfs(TreeNode root) {
        queue.add(new Pair(root, 0));

        while(!queue.isEmpty()) {
            Pair cur = queue.poll();
            TreeNode curNode = cur.node;

            if (cur.level > maxLevel) {
                maxLevel = cur.level;
                ans = curNode.val;
            }

            if (curNode.left != null) queue.add(new Pair(curNode.left, cur.level + 1));
            if (curNode.right != null) queue.add(new Pair(curNode.right, cur.level + 1));
        }
    }
}
