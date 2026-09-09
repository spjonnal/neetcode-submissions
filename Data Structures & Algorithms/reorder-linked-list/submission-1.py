# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        slow = fast= head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow has second half - reverse it
        rev = None # this will be reverse
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = rev
            rev = cur
            cur = temp
        first = head
        second = rev
        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            second = t2
            first = t1




        
