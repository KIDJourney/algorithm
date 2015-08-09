/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if (!head or !head->next) 
            return head;
        ListNode* ansnode = new ListNode(0);;
        while (head) {
            ListNode * posnode = ansnode;
            while (posnode->next and posnode->next->val <= head->val)
                posnode = posnode->next;
            ListNode * nextnode = posnode->next;
            posnode->next = head;
            head = head->next;
            posnode->next->next = nextnode;
            
        }
        return ansnode->next;
    }
};