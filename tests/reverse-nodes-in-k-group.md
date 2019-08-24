# 25. Reverse Nodes in k-Group

* *Difficulty: Hard*

* *Topics: Linked List*

* *Similar Questions:*

  * [Swap Nodes in Pairs](./tests/reverse-nodes-in-k-group.md)

## Problem:

<p>Given a linked list, reverse the nodes of a linked list <em>k</em> at a time and return its modified list.</p>

<p><em>k</em> is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of <em>k</em> then left-out nodes in the end should remain as it is.</p>

<ul>
</ul>

<p><strong>Example:</strong></p>

<p>Given this linked list: <code>1-&gt;2-&gt;3-&gt;4-&gt;5</code></p>

<p>For <em>k</em> = 2, you should return: <code>2-&gt;1-&gt;4-&gt;3-&gt;5</code></p>

<p>For <em>k</em> = 3, you should return: <code>3-&gt;2-&gt;1-&gt;4-&gt;5</code></p>

<p><strong>Note:</strong></p>

<ul>
	<li>Only constant extra memory is allowed.</li>
	<li>You may not alter the values in the list&#39;s nodes, only nodes itself may be changed.</li>
</ul>

## Solutions:

```c++
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head)  return NULL;
        //cout << "head" << head->val << endl;
        ListNode* tail = head;
        ListNode* current;
        ListNode* previous;
        ListNode* next;
        ListNode* returnHead;
        ListNode* current_next;
        ListNode* previous_next;
        int count = k;
        
        ListNode* dummyHead = new ListNode(0);
        dummyHead -> next = head;
        while (((--count) > 0) && tail)
        {
            tail = tail -> next;
        }
       // cout << "tail" << tail->val << endl;
        if (!tail)  return head;
        next = tail -> next;
        previous = dummyHead;
        current = head;
        
        while (previous != tail)
        {
             //cout << current-> val << endl;
            //if (current ->val == 0)  {cout << current << endl; break;}
            current_next = current -> next;
            previous_next = current;
            current -> next = previous;
            current = current_next;
            previous = previous_next;
        }
        //cout << "next" << next->val << endl;
        dummyHead -> next -> next = reverseKGroup (next, k);
        delete dummyHead;
        return tail;
    }
};
```
