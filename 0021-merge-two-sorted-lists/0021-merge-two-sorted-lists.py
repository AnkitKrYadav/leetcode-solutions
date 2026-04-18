# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head 
        lt1 = list1 
        lt2 = list2
        while lt1 and lt2:
            if lt1.val < lt2.val:
                tail.val = lt1.val
                lt1 = lt1.next
                tail.next = ListNode()
                tail = tail.next

            else: 
                tail.val = lt2.val
                lt2 = lt2.next
                tail.next = ListNode()
                tail = tail.next
        if lt1:
            tail.val = lt1.val
            tail.next = lt1.next
            return head
        elif lt2:
            tail.val = lt2.val
            tail.next = lt2.next
            return head
        return None
