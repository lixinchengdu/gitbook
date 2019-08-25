# 206. Reverse Linked List

* *Difficulty: Easy*

* *Topics: Linked List*

* *Similar Questions:*

  * [Reverse Linked List II](reverse-linked-list-ii.md)

  * [Binary Tree Upside Down](binary-tree-upside-down.md)

  * [Palindrome Linked List](palindrome-linked-list.md)

## Problem:

<p>Reverse a singly linked list.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL
<strong>Output:</strong> 5-&gt;4-&gt;3-&gt;2-&gt;1-&gt;NULL
</pre>

<p><b>Follow up:</b></p>

<p>A linked list can be reversed either iteratively or recursively. Could you implement both?</p>

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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        ListNode* reverseSubList = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return reverseSubList;
    }
};
```
