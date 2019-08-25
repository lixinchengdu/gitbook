# 19. Remove Nth Node From End of List

* *Difficulty: Medium*

* *Topics: Linked List, Two Pointers*

* *Similar Questions:*

## Problem:

<p>Given a linked list, remove the <em>n</em>-th node from the end of list and return its head.</p>

<p><strong>Example:</strong></p>

<pre>
Given linked list: <strong>1-&gt;2-&gt;3-&gt;4-&gt;5</strong>, and <strong><em>n</em> = 2</strong>.

After removing the second node from the end, the linked list becomes <strong>1-&gt;2-&gt;3-&gt;5</strong>.
</pre>

<p><strong>Note:</strong></p>

<p>Given <em>n</em> will always be valid.</p>

<p><strong>Follow up:</strong></p>

<p>Could you do this in one pass?</p>

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* front = head;
        for (int i = 0; i < n; ++i) {
            if (front == NULL)  return NULL;
            front = front->next;
        }
        
        if (front == NULL) {
            return head->next;
        }
        
        front = front->next;
        
        ListNode* cur = head;
        while (front != NULL) {
            front = front->next;
            cur = cur->next;
        }
        
        cur->next = cur->next->next;
        return head;
        
    }
};
```
