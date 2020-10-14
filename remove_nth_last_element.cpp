class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        ListNode** match = &head;
        ListNode* prev;

        for(int i = 0; i < n; i++)
            first = first->next;

        while(first){
            first = first->next;
            match = &((*match)->next);
        }

        ListNode* node = *match;
        *match = node->next;

        delete node;

        return head;
    }
};
