def detectCycle(head):
    slow = fast = head

    while fast and fast.next and fast != slow:
        slow = slow.next
        fast = fast.next 
        if fast.next:
            fast = fast.next
    
    if fast == None or fast.next == None:
        return None

    while head != slow:
        head = head.next
        slow = slow.next

    return slow