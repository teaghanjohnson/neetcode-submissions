# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # iterate through list to get length
        length = 0       
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head

        prevGroupTail = dummy
        curr = head

        groups = length // k

        for _ in range(groups):
            groupStart = curr
            prev = None

            #reverse k nodes
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # after reversal:
            # prev = new group head
            # groupStart = new group tail
            # curr = next group start

              
            # [3,2,1,4,5,6]
            prevGroupTail.next = prev
            groupStart.next = curr

            prevGroupTail = groupStart
            
        return dummy.next
        
    