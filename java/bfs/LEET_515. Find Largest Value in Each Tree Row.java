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

    private List<Integer> ans = new ArrayList<>();
    private int maxLevel = 0;
    private int maxVal = Integer.MIN_VALUE;

    public List<Integer> largestValues(TreeNode root) {
        if (root == null) return new ArrayList<Integer>();

        bfs(root);
        return ans;
    }

    private void bfs(TreeNode root) {

        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(root, 0));

        while(!queue.isEmpty()) {

            Pair cur = queue.poll();

            // if it is on new level, save and reset minVal
            if (cur.level > maxLevel) {
                ans.add(maxVal);
                maxVal = Integer.MIN_VALUE;
                ++maxLevel;
            }

            // set maxVal to max value of the level
            maxVal = Math.max(maxVal, cur.node.val);

            if (cur.node.left != null)
                queue.add(new Pair(cur.node.left, cur.level + 1));
            if (cur.node.right != null)
                queue.add(new Pair(cur.node.right, cur.level + 1));

        }
        ans.add(maxVal);

    }
}
