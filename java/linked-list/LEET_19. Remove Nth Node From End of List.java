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

    // private List<ListNode> arr = new ArrayList<>();

    public ListNode removeNthFromEnd(ListNode head, int n) {
        return helper(head, n);   
        
    }

    // not working bc of TLE

    // private ListNode helper(ListNode head, int n) {
    //     ListNode cur = head;

    //     // add nodes in arr
    //     while (cur != null) {
    //         arr.add(cur);
    //         cur = cur.next;
    //     }

    //     // find nth node from backward
    //     int i = arr.size() - 1;
    //     while (n != 0) --i;
        
    //     // connect
    //     arr.get(i - 1).next = arr.get(i + 1);

    //     return head;
        
    // }

    private ListNode helper(ListNode head, int n) {
        
        ListNode start = new ListNode();
        start.next = head;
        ListNode fast = start;
        ListNode slow = start;

        for(int i = 0; i < n; i++) {
            fast = fast.next;
        }

        while(fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        
        return start.next;
    }

}
