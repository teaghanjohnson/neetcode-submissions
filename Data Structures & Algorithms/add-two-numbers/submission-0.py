# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # while curr_1 and curr_2 are not null
        # add values to array in reverse order
        # compute answer
        # add new Listnode add answer in reverse order

        carry = 0
        dummy = ListNode()
        current= dummy
    
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            digit = sum % 10
            carry = sum // 10
            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        
        return dummy.next
