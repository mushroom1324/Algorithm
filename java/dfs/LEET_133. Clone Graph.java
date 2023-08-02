/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {

    private void dfs(Node node, Node copy, Node[] visited) {

        // visited를 hashMap처럼 사용
        visited[copy.val] = copy;

        for (Node each : node.neighbors) {

            // 방문하지 않은 노드면 새로 만듦
            if (visited[each.val] == null) {
                Node newNode = new Node(each.val);

                copy.neighbors.add(newNode);

                // 만든 노드를 dfs
                dfs(each, newNode, visited);
            }
            else {
                // 방문한 노드면 이웃에 넣음
                copy.neighbors.add(visited[each.val]);
            }
        }
    }


    public Node cloneGraph(Node node) {
        if (node == null) return node;
        Node copy = new Node(node.val);
        Node[] visited = new Node[101];
        Arrays.fill(visited, null);
        dfs(node, copy, visited);
        return copy;
    }
}
