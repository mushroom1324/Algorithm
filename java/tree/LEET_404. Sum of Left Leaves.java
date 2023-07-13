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
    public boolean isLeft;
    public TreeNode node;

    Pair(boolean isLeft, TreeNode node) {
        this.isLeft = isLeft;
        this.node = node;
    }
}

class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        int ans = 0;
        Queue<Pair> queue = new LinkedList<>();

        queue.add(new Pair(false, root));

        while(!queue.isEmpty()) {
            boolean flag = false;
            Pair cur = queue.poll();

            if (cur.node.left != null) {
                queue.add(new Pair(true, cur.node.left));
                flag = true;
            }
            if (cur.node.right != null) {
                queue.add(new Pair(false, cur.node.right));
                flag = true;
            }

            if (!flag && cur.isLeft) ans += cur.node.val;

        }
        return ans;
    }
}