/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    private int len;
    private Stack<ListNode> stack = new Stack<>();

    public void reorderList(ListNode head) {

        // put all elements to the stack.
        ListNode cur = head;
        
        while ( cur != null ) {
            stack.add(cur);
            cur = cur.next;
            ++len;
        }

        // insert the top node of the stack accordingly.
        // repeat it (len // 2) times.
        cur = head;

        for(int i = 0; i < len / 2 ; ++i) {
            ListNode temp = cur.next; 
            ListNode endNode = stack.pop(); 
            cur.next = endNode; 
            endNode.next = temp; 
            cur = temp; 
        }
        
        // delete cycle of the last node.
        cur.next = null;
        
    }
}
