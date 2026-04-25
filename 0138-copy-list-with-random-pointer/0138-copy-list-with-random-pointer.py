"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        chead = Node(head.val)
        l1 = head.next
        l2  = chead
        l2i = {0:chead}
        pos,p = {head:0},1
        #copy list node with next pointer only
        while l1:
            pos[l1] = p
            l2.next = Node(l1.val)
            l1 = l1.next
            l2 = l2.next
            l2i[p] = l2
            p += 1
        l1 = head
        l2 = chead

        # copy random pointers
        while l1:
            if l1.random != None:
                k = pos[l1.random]
                l2.random = l2i[k]
            l1 = l1.next
            l2 = l2.next
        return chead
#O(n^2)                         
        