# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        curr = head
        p = 1
        if n == k:
            head = head.next
            return head
        while p <= n-k:
            if p == n-k:
               curr.next = curr.next.next
               return head               
            curr = curr.next
            p += 1        
    #O(N)