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

    private Queue<TreeNode> queue = new LinkedList<>();
    private StringBuilder sb = new StringBuilder();

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";

        serizalizeHelper(root);

        return sb.toString();
        
    }

    private void serizalizeHelper(TreeNode root) {

        queue.add(root);

        while (!queue.isEmpty()) {

            TreeNode node = queue.poll();

            if (node == null) sb.append("n,");
            else {
                sb.append(String.valueOf(node.val)).append(",");

                queue.add(node.left);
                queue.add(node.right);
            }
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

        String[] arr = data.split(",");

        if (data == "") return null;

        TreeNode ans = new TreeNode(Integer.parseInt(arr[0]));
        queue.add(ans);
        
        for (int i = 1; i < arr.length - 1; ++i) {
            TreeNode node = queue.poll();

            if (!arr[i].equals("n")) {
                TreeNode left = new TreeNode(Integer.parseInt(arr[i]));
                node.left = left;
                queue.add(left);
            }
            if (!arr[++i].equals("n")) {
                TreeNode right = new TreeNode(Integer.parseInt(arr[i]));
                node.right = right;
                queue.add(right);
            }
        }        
        return ans;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
