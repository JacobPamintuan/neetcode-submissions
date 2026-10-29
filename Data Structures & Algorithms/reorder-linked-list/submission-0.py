# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Middle of list
        slow = fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        # Reverse second half
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n

        l1 = head
        l2 = prev

        while l1 and l2:
            next1 = l1.next
            next2 = l2.next

            l1.next = l2
            l2.next = next1

            l1 = next1
            l2 = next2



        

