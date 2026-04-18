# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head 
        while list1 and list2:
            if list1.val < list2.val:
                tail.val = list1.val
                list1 = list1.next
                tail.next = ListNode()
                tail = tail.next

            else: 
                tail.val = list2.val
                list2 = list2.next
                tail.next = ListNode()
                tail = tail.next
        if list1:
            tail.val = list1.val
            tail.next = list1.next
            return head
        elif list2:
            tail.val = list2.val
            tail.next = list2.next
            return head
        return None
#O(n+m)
