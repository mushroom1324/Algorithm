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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;

        List<Integer> arr = new ArrayList<>();
        
        ListNode cur = head;
    
        while(cur != null) {
            arr.add(cur.val);
            cur = cur.next;
        }
        List<Integer> newArr = arr.stream().distinct().collect(Collectors.toList());

        Collections.sort(newArr);
    
        ListNode ans = new ListNode();
        ListNode ansHead = ans;

        int i = 0;
        while(i < newArr.size() - 1) {
            ans.val = newArr.get(i);
            ans.next = new ListNode();
            ans = ans.next;
            i++;
        }
        ans.val = newArr.get(i);

        return ansHead;
    }
}
