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
    public TreeNode deleteNode(TreeNode root, int key) {
        return traverse(root, key);
    }


    private TreeNode traverse(TreeNode root, int key) {
        if (root == null) return root;
        if (key < root.val) root.left = traverse(root.left, key);
        else if (key > root.val) root.right = traverse(root.right, key);
        else {
            // 왼쪽이 비었을 경우 오른쪽 노드로 대체
            if (root.left == null) return root.right;
            // 오른쪽이 비었을 경우 왼쪽 노드로 대체
            else if (root.right == null) return root.left;
            // 양쪽 다 있는 경우 오른쪽 가지의 가장 왼쪽 노드
            root.val = minVal(root.right);
            root.right = traverse(root.right, root.val);
        }
        return root;
    }

    // 가장 왼쪽 노드 값 가져옴(최소)
    private int minVal(TreeNode node) {
        int min = node.val;
        while (node.left != null) {
            min = node.left.val;
            node = node.left;
        }
        return min;
    }
}
