# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # exception for #node = 0
        if not head:
            return True

        # slow, and fast pointers to make space complexity O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # making reverse linked list throught [mid:last]
        prev = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = prev
            prev = cur

        # check if it is palindrome
        while prev:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next

        return True

