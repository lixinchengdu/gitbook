# 92. Reverse Linked List II

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

  * [Reverse Linked List](reverse-linked-list.md)

## Problem:

<p>Reverse a linked list from position <em>m</em> to <em>n</em>. Do it in one-pass.</p>

<p><strong>Note:&nbsp;</strong>1 &le; <em>m</em> &le; <em>n</em> &le; length of list.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL, <em>m</em> = 2, <em>n</em> = 4
<strong>Output:</strong> 1-&gt;4-&gt;3-&gt;2-&gt;5-&gt;NULL
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == nullptr)    return nullptr;
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* cur = dummy;
        int index = 0;
        
        while (cur && index < m - 1) {
            cur = cur->next;
            ++index;
        }
        
        ListNode* tail = cur;
        cur = cur->next;
        ListNode* reverseLast = cur;
        tail->next = nullptr;
        
        for (int i = 0; i < n - m + 1; ++i) {
            ListNode* next = cur->next;
            cur->next = tail->next;
            tail->next = cur;
            cur = next;
        }
        
        reverseLast->next = cur;
        
        return dummy->next;
        
    }
};
```
