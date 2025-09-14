# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        n = head
        
        while n and n.next:
            p = p.next
            n = n.next.next
            
            if p == n:
                return True
            
        return False