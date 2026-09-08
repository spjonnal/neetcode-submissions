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

        new = ListNode(0)
        out  = new
        while list1 or list2:
            if list1 and not list2:
                new.next = list1
                list1 = list1.next
                new = new.next
            elif list2 and not list1:
                new.next = list2
                list2 = list2.next
                new = new.next
            else:
                if list1.val <= list2.val:
                    new.next = list1
                    list1 = list1.next
                    new = new.next
                else:
                    new.next = list2
                    list2 = list2.next
                    new = new.next
        return out.next

