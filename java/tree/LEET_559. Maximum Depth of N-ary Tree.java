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

    private int max = 0;

    public int maxDepth(Node root) {
        
        helper(root, 1);
        return max;
    }

    private void helper(Node node, int cnt) {
        if (node == null) return;
        max = Math.max(max, cnt);

        node.children.forEach(each -> helper(each, cnt + 1));

    }
}
