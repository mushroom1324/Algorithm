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

    private List<Long> list = new ArrayList<>();
    private Queue<TreeNode> queue = new LinkedList<>();
    private int level = -1;
    private int cnt = 1;
    private int nextCnt = 1;

    public long kthLargestLevelSum(TreeNode root, int k) {
        
        queue.add(root);

        while (!queue.isEmpty()) {

            TreeNode cur = queue.poll();

            if (--cnt == 0) {
                ++level;
                cnt = nextCnt;
                nextCnt = 0;
                list.add(0L);
            }

            list.set(level, list.get(level) + cur.val);

            if (cur.left != null) {
                queue.add(cur.left);
                ++nextCnt;
            }
            if (cur.right != null) {
                queue.add(cur.right);
                ++nextCnt;
            } 
            
        }

        Collections.sort(list, Collections.reverseOrder());

        if (k > list.size()) return -1;

        return list.get(k - 1);

    }
}
