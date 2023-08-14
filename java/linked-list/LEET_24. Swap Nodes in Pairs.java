/**
 * Beats 100.00%of users with Java LOL 
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
    public ListNode swapPairs(ListNode head) {

        // base cases
        if (head == null || head.next == null) return head;

        // init with prev and cur
        ListNode prev = head;
        ListNode cur = head.next;

        // point the right head
        head = cur;
        
        while(cur != null) {
            System.out.println(prev.val);
            System.out.println(cur.val);

            ListNode temp = cur.next;

            // if not null, swap
            if (cur.next == null || cur.next.next == null) 
                prev.next = cur.next;
            else prev.next = cur.next.next;
            cur.next = prev;

            // point next two nodes
            prev = temp;
            if (prev == null) break;
            cur = prev.next;

        }
        
        return head;

    }
}
