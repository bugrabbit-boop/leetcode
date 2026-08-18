# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for _ in range(n):
            slow=slow.next
        if not slow:
            return head.next
        
        while slow.next:
            slow=slow.next
            fast=fast.next

        fast.next=fast.next.next
        return head



        