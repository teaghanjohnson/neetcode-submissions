# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # iterate over all arrays lists[i][j]
        # store all values in a set(), (make it in order?)

        #iterate over each value in set linking values based upon each occurence 

        seen = {}
        dummy = ListNode(0)
        current = dummy
        for head in lists:
            node = head
            while node:
                seen[node.val] = seen.get(node.val, 0) + 1
                node = node.next

        seen_sorted = dict(sorted(seen.items()))

        for val in seen_sorted:
            total = seen_sorted[val]
            for _ in range(total):
                current.next = ListNode(val)
                current = current.next

        return dummy.next

