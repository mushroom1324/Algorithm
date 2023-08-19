/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {

    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> temp = new ArrayList<>();
    private int level = 1;
    private int next = 0;

    public List<List<Integer>> levelOrder(Node root) {
        if (root == null) return ans;
        bfs(root);
        return ans;
    }

    private void bfs(Node node) {

        Queue<Node> queue = new LinkedList<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            Node cur = queue.poll();

            temp.add(cur.val);

            cur.children.forEach(each -> {
                queue.add(each);
                ++next;
            });
            
            if (--level == 0) {
                level = next;
                next = 0;
                ans.add(temp);
                temp = new ArrayList<>();
            }           

        }

    }
}
