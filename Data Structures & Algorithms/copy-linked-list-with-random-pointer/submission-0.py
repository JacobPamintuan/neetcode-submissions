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
        
        dummy = Node(0)
        curr = dummy

        mp = {}

        old = head

        while old:
            curr.next = Node(old.val, None, None)
            curr = curr.next

            mp[old] = curr
            old = old.next

        curr = dummy.next
        old = head

        while old:
            curr.random = mp[old.random] if old.random else None
            curr = curr.next
            old = old.next

        return dummy.next

        