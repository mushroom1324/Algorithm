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

    private int maxVal = -10000;

    public int maxPathSum(TreeNode root) {
        maxVal = Math.max(helper(root), maxVal);
        return maxVal;
    }

    private int helper(TreeNode node) {

        if (node.left == null && node.right == null) {
            maxVal = Math.max(maxVal, node.val);
            return node.val;
        }

        // 한쪽만 null일 때
        else if (node.left == null) {
            int rightMost = helper(node.right);
            maxVal = Math.max(node.val + rightMost, maxVal);
            maxVal = Math.max(node.val, maxVal);
            if (rightMost > 0) return node.val + rightMost;
            else return node.val;
        }
        else if (node.right == null) {
            int leftMost = helper(node.left);
            maxVal = Math.max(node.val + leftMost, maxVal);
            maxVal = Math.max(node.val, maxVal);
            if (leftMost > 0) return node.val + leftMost;
            else return node.val;
        }


        // 둘 다 있을 때 
        int leftMost = helper(node.left);
        int rightMost = helper(node.right);
        
        // sum : 양쪽 + 현재 노드
        int sum = node.val + leftMost + rightMost;

        // 최댓값 갱신
        maxVal = Math.max(maxVal, node.val);
        maxVal = Math.max(maxVal, sum);
        maxVal = Math.max(maxVal, leftMost);
        maxVal = Math.max(maxVal, rightMost);
        maxVal = Math.max(maxVal, leftMost + node.val);
        maxVal = Math.max(maxVal, rightMost + node.val);


        // 양쪽 다 음수인 경우
        if (Math.max(leftMost, rightMost) < 0) return node.val;
        // 둘중 더 큰쪽과 현재 노드를 반환
        return node.val + Math.max(leftMost, rightMost);

    }
}
