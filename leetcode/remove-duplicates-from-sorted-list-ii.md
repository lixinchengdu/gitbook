# 82. Remove Duplicates from Sorted List II

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

  * [Remove Duplicates from Sorted List](remove-duplicates-from-sorted-list.md)

## Problem:

<p>Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only <em>distinct</em> numbers from the original list.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;3-&gt;3-&gt;4-&gt;4-&gt;5
<strong>Output:</strong> 1-&gt;2-&gt;5
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;1-&gt;1-&gt;2-&gt;3
<strong>Output:</strong> 2-&gt;3
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* tail = dummyHead;
        ListNode* cur = head;
        
        while (cur) {
            if (cur->next && cur->val == cur->next->val) {
                int val = cur->val;
                cur = cur->next->next;
                while (cur && cur->val == val) {
                    cur = cur->next;
                }
            } else {
                tail->next = cur;
                tail = cur;
                cur = cur->next;
            }
        }
        
        tail->next = NULL;
        
        return dummyHead->next;
        
    }
};
```
