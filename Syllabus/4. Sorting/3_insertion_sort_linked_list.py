def insertion_sort_linked_list(head):
  curr = Node()
  curr.next = head
  while curr:
    node_to_insert = curr.next
    curr.next = curr.next.next
    runner = head

    while node_to_insert.val < runner.next.val and runner != curr:
      runner = runner.next
    
    node_to_insert.next = runner.next
    runner.next = node_to_insert.next

    curr = curr.next

  return head