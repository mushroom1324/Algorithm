/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {

    private HashMap<ListNode, Boolean> map = new HashMap<>();

    public ListNode detectCycle(ListNode head) {    
        ListNode cur = head;

        while (cur != null) {

            if (map.containsKey(cur)) {
                // cycle found
                return cur;
                   
            } else {
                map.put(cur, true);    
            }

            cur = cur.next;
        }

        return null;
        
    }
}
