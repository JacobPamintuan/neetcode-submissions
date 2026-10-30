# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            val = add % 10
            carry = add // 10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        last = l1 if l1 else l2

        while last:
            add = last.val + carry
            val = add % 10
            carry = add // 10

            curr.next = ListNode(val)
            curr = curr.next
            last = last.next
        
        if carry:
            curr.next = ListNode(carry)


        
        return dummy.next
