# 24. Swap Nodes in Pairs

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

  * [Reverse Nodes in k-Group](reverse-nodes-in-k-group.md)

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
        ListNode* dummyHead = new ListNode(0);
        ListNode* tail = dummyHead;
        while (head && head->next) {
            ListNode* first = head;
            ListNode* second = head->next;
            head = head->next->next; // remember to the head of next round intermidiately
            tail->next = second;
            second->next = first;
            tail = first;
            tail->next = nullptr;
        }
        
        if (head) {
            tail->next = head;
        }
        
        return dummyHead->next;
    }
};
```
