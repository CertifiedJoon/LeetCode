class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stck = []
        slow = fast = head
        l = 0
        while fast:
            stck.append(slow.val)
            slow = slow.next
            fast = fast.next
            l += 1
            if fast:
                l += 1
                fast = fast.next

        if l % 2 == 1:
            stck.pop()

        while slow:
            if stck.pop() != slow.val:
                return False
            slow = slow.next
        
        return True