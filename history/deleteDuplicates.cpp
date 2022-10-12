class Solution{
public:
  ListNode *deleteDuplicates(ListNode* head){
    ListNode* current = head;

    while(current && current->next != nullptr){
      if (current->next->val == current->val){
        ListNode* node = current->next;
        current->next = node->next;
        delete node;
      }
      else
        current = current->next;
    }
    return head;
  }
};
