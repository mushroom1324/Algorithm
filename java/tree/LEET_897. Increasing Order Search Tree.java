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

    private ArrayList<TreeNode> arr=new ArrayList<>();

    public TreeNode increasingBST(TreeNode root) {
        if(root==null) return null;
        
        inorder(root);

        for(int i=0;i<arr.size()-1;i++){

            arr.get(i).right=arr.get(i+1);
            arr.get(i).left=null;

        }

        arr.get(arr.size()-1).left=null;
        arr.get(arr.size()-1).right=null;

        return arr.get(0);
    }

    private void inorder(TreeNode node){
        if(node==null) return;
        
        inorder(node.left);
        arr.add(node);
        inorder(node.right);

    }
}
