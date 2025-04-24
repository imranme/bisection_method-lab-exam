class Solution {
public:
void insert_tail(ListNode *&head,ListNode*&tail,int val){
ListNode *newNode=new ListNode(val);
if(head==NULL){
head=newNode;
tail=newNode;
return;
}
tail->next=newNode;
tail=newNode;
}
void reverse(ListNode *&head,ListNode *curr){
if(curr->next==NULL){
head=curr;
return;
}
reverse(head,curr->next);
curr->next->next=curr;
curr->next=NULL;
}
bool isPalindrome(ListNode* head) {
ListNode *newhead=NULL;
ListNode *newtail=NULL;
ListNode *tmp=head;
while(tmp!=NULL){
insert_tail(newhead,newtail,tmp->val);
}
reverse(newhead,newhead);
ListNode *tmp2=newhead;
while(tmp!=NULL){
if(tmp->val!=tmp2->val){
return false;
}
tmp=tmp->next;
tmp2=tmp2->next;
}
return true;
}
};
palindrome linked list er problem eita, amr ei code e problem ki hoice .time limit exceeded hocce keno?

