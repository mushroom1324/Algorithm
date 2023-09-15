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
    TreeNode node;
    int cnt;
    List<Integer> list;

    Pair(TreeNode node, int cnt, List<Integer> list) {
        this.node = node;
        this.cnt = cnt;
        this.list = list;
    }
}

class Solution {

    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if( root == null ) return new ArrayList<>();
        bfs(root, targetSum);

        return ans;
    }

    private void bfs(TreeNode root, int targetSum) {
        Queue<Pair> queue = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        list.add(root.val);
        queue.add(new Pair(root, root.val, new ArrayList<>(list)));

        while (!queue.isEmpty()) {
            Pair cur = queue.poll();
            List<Integer> curList = new ArrayList<>(cur.list);

            if (cur.node.left == null && cur.node.right == null && cur.cnt == targetSum) {
                ans.add(curList);
                continue;
            }

            if (cur.node.left != null) {
                List<Integer> leftList = new ArrayList<>(curList);
                leftList.add(cur.node.left.val);
                queue.add(new Pair(cur.node.left, cur.cnt + cur.node.left.val, leftList));
            }
            if (cur.node.right != null) {
                List<Integer> rightList = new ArrayList<>(curList);
                rightList.add(cur.node.right.val);
                queue.add(new Pair(cur.node.right, cur.cnt + cur.node.right.val, rightList));
            }
        }
    }
}
