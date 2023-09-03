/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    private StringBuilder sb = new StringBuilder();

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        sb.append('[');
        traverse(root);
        sb.deleteCharAt(sb.length() - 1).append(']');
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        
        Deque<String> queue = new LinkedList<>();

        data = data.replace("[", "");
        data = data.replace("]", "");


        queue.addAll(Arrays.asList(data.split(",")));

        return addTree(queue);
    }

    private void traverse(TreeNode node) {
        if (node == null) {
            sb.append("x,");
            return;
        }
        
        sb.append(node.val).append(',');

        traverse(node.left);
        traverse(node.right);
    }

    private TreeNode addTree(Deque<String> queue) {
        String res = queue.remove();

        if(res.equals("x")){
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(res));

        root.left = addTree(queue);
        root.right = addTree(queue);

        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
