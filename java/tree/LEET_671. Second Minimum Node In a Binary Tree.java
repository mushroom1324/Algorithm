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

    private List<Integer> arr = new ArrayList<>(); 
    private List<Integer> newArr = new ArrayList<>(); 

    public int findSecondMinimumValue(TreeNode root) {
        inOrder(root);

        Collections.sort(arr);

        arr.forEach(each -> {
            if (!newArr.contains(each)) newArr.add(each); 
        });

        if (newArr.size() == 1) return -1;
        return newArr.get(1);
    }

    private void inOrder(TreeNode node) {
        
        if (node.left != null)
            inOrder(node.left);

        arr.add(node.val);

        if (node.right != null)
            inOrder(node.right);
    }
}
