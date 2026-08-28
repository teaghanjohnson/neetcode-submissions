# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        hasSeen = []
        i = 0

        if head == None:
            return False
            
        while head.next:
            if head.val not in hasSeen:
                hasSeen.append(head.val)
                head = head.next
                index += 1
            else:
                return True
        
        return False

        # iterate through list, track length if end points to value see what value matches that in array index equals position of that valie loop equals true
