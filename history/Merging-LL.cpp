#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
  struct ListNode{
    int val;
    ListNode *next;
  };

  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
    ListNode head(0), *current = &head;
    while(l1 || l2){
      if(l1 && l2){
        if (l1->val <= l2->val){
          current->next = new ListNode (l1->val);
          current = current->next;
          l1 = l1->next;
        }
        else if (l1->val > l2->val){
          current->next = new ListNode (l2->val);
          current = current->next;
          l2 = l2->next;
        }
      }
      else if (l1 && !l2){
        current->next = new ListNode (l1->val);
        current = current->next;
        l1 = l1->next;
      }
      else if (l2 && !l1){
        current->next = new ListNode (l2->val);
        current = current->next;
        l2 = l2->next;
      }
    }
  return head.next;
  }
};
