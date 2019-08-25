# 148. Sort List

* *Difficulty: Medium*

* *Topics: Linked List, Sort*

* *Similar Questions:*

  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)

  * [Sort Colors](sort-colors.md)

  * [Insertion Sort List](insertion-sort-list.md)

## Problem:

<p>Sort a linked list in <em>O</em>(<em>n</em> log <em>n</em>) time using constant space complexity.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 4-&gt;2-&gt;1-&gt;3
<strong>Output:</strong> 1-&gt;2-&gt;3-&gt;4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -1-&gt;5-&gt;3-&gt;4-&gt;0
<strong>Output:</strong> -1-&gt;0-&gt;3-&gt;4-&gt;5</pre>

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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr)    return nullptr;
        if (head->next == nullptr)  return head;
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast->next !=  nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        ListNode* head2 = slow->next;
        slow->next = nullptr;
        
        ListNode* leftHead = sortList(head);
        ListNode* rightHead = sortList(head2);
        
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        
        while (leftHead != nullptr && rightHead != nullptr) {
            if (leftHead->val < rightHead->val) {
                tail->next = leftHead;
                tail = leftHead;
                leftHead = leftHead->next;
            } else {
                tail->next = rightHead;
                tail = rightHead;
                rightHead = rightHead->next;
            }
        }
        
        if (leftHead == nullptr) {
            tail->next = rightHead;
        } else {
            tail->next = leftHead;
        }
        
        return dummy->next;
    }
};
```
