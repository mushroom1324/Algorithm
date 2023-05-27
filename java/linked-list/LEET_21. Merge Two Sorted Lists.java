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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list3 = new ListNode();
        ListNode listHeader = list3;
        System.out.println(list3);
        while (list1 != null && list2 != null) {
            list3.next = new ListNode();
            list3 = list3.next;
            if (list1.val >= list2.val) {
                System.out.println(list2.val);
                list3.val = list2.val;
                list2 = list2.next;
            } else {
                System.out.println(list1.val);
                list3.val = list1.val;
                list1 = list1.next;
            }
        }
        while (list1 != null) {
            list3.next = new ListNode();
            list3 = list3.next;
            list3.val = list1.val;
            list1 = list1.next;
        }
        while (list2 != null) {
            list3.next = new ListNode();
            list3 = list3.next;
            list3.val = list2.val;
            list2 = list2.next;
        }

        return listHeader.next;
    }
}


