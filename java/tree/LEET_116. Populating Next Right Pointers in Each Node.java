/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {

        Queue<Node> level = new LinkedList<>();
        Queue<Node> next_level = new LinkedList<>();

        level.add(root);
        while (true) {
            while (level.peek() != null) {
                Node cur = level.poll();

                if (cur.left != null) {
                    next_level.add(cur.left);
                }
                if (cur.right != null) {
                    next_level.add(cur.right);
                }

                cur.next = level.peek();

            }
            if (next_level.peek() == null) break;
            while (next_level.peek() != null) {
                level.add(next_level.poll());
            }

        }

        return root;

    }
}