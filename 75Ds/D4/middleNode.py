def middleNode(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if fast.next:
            fast = fast.next
    
    return slow