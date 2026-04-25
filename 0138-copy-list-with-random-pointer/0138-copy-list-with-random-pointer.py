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
    
        copy = Node(head.val)
        l1,l2 = head.next, copy
        l2i,l1pos,p = {0:copy},{head:0},1
        
        #copy list node with next pointer only
        while l1:
            l1pos[l1] = p
            l2.next = Node(l1.val)

            l1 = l1.next
            l2 = l2.next

            l2i[p] = l2

            p += 1
        #reset iterators    
        l1 = head
        l2 = copy

        # copy random pointers
        while l1:
            if l1.random != None:
                k = l1pos[l1.random]
                l2.random = l2i[k]
            l1 = l1.next
            l2 = l2.next
        return copy
#O(n)  can be also done using existing node in old2new dic and later joining them                       
        