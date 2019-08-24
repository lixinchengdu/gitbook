# 24. Swap Nodes in Pairs

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

  * [Reverse Nodes in k-Group](./tests/swap-nodes-in-pairs.md)

## Problem:

<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head.</p>

<p>You may <strong>not</strong> modify the values in the list&#39;s nodes, only nodes itself may be changed.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
Given <code>1-&gt;2-&gt;3-&gt;4</code>, you should return the list as <code>2-&gt;1-&gt;4-&gt;3</code>.
</pre>

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
    ListNode* swapPairs(ListNode* head) {
        ListNode* pre = NULL;
        ListNode* cur = head;
        ListNode* newhead = NULL;
        int counter = 0;
        if (!head)  return head;
        if (!head->next)    return head;
        newhead = head->next;
        head->next = newhead->next;
        newhead -> next = head;
        
        cur = head;
        pre = head;
        
        while (cur->next)
        {
            cur = cur-> next;
            if (!(++counter % 2))
            {
                ListNode* mid = pre->next;
                pre->next = cur;
                mid->next = cur -> next;
                cur->next = mid;
                pre = mid;
                cur = mid;
            }
        }
     return newhead;   
    }
};
```
