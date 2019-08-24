# 206. Reverse Linked List

* *Difficulty: Easy*

* *Topics: Linked List*

* *Similar Questions:*

  * [Reverse Linked List II](./tests/reverse-linked-list.md)

  * [Binary Tree Upside Down](./tests/reverse-linked-list.md)

  * [Palindrome Linked List](./tests/reverse-linked-list.md)

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
        if (!head)  return NULL;
        if (head->next == NULL) return head;
        ListNode* nextNode = head->next;
        ListNode* first = reverseList(nextNode);
        nextNode->next = head;
        head->next = NULL;
        return first;
    }
};
```
