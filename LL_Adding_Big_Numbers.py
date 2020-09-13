# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):                #__init__ initiates as soon as the class is called
       self.val = val
       self.next = next                                 #self function's member variables can be accessed publicly
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = current = ListNode(0)                      # res = ListNode() -> calls __init__ function and assign 0 as val;
        while l1 or l2 or carry:                         # then current = same address(val = 0)
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            current.next = current = ListNode(val)      #current.next = ListNode(val), then, current = same address
        return res.next #since first element was declared as 0; we return res.next
