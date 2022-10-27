# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = ListNode(None, head)
        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        if slow.next == head:
            head = head.next
        else:
            slow.next = slow.next.next if slow.next else None

        return head