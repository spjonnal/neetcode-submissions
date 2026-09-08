# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and list2:
            return None
        l1 = list1
        l2 = list2
        new = ListNode(0)
        out  = new
        while l1 or l2:
            if l1 and not l2:
                new.next = l1
                l1 = l1.next
                new = new.next
            elif l2 and not l1:
                new.next = l2
                l2 = l2.next
                new = new.next
            else:
                if l1.val <= l2.val:
                    new.next = l1
                    l1 = l1.next
                    new = new.next
                else:
                    new.next = l2
                    l2 = l2.next
                    new = new.next
                
        return out.next

