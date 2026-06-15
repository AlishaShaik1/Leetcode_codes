/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    int count=0;
    struct ListNode*p=head;
    while(p!=NULL){
        count++;
        p=p->next;
    }
    int mid=count/2;
    if(mid==0){
        return NULL;
    }
    p=head;

    for(int i=0;i<mid-1;i++){
        p=p->next;
    }
    struct ListNode* temp = p->next;
    p->next = p->next->next;
    free(temp);

    return head;
}