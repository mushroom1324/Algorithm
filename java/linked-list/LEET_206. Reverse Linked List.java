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
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        Stack<ListNode> stack = new Stack<>();

        ListNode cur = head;

        while(cur != null) {
            stack.push(cur);
            cur = cur.next;
        }

        cur = stack.peek();

        while (!stack.isEmpty()) {
            ListNode revCur = stack.pop();
            if (stack.isEmpty()) revCur.next = null;
            else revCur.next = stack.peek();
        }

        return cur;

    }
}
