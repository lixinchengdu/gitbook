# 203. Remove Linked List Elements

* *Difficulty: Easy*

* *Topics: Linked List*

* *Similar Questions:*

  * [Remove Element](remove-element.md)

  * [Delete Node in a Linked List](delete-node-in-a-linked-list.md)

## Problem:

<p>Remove all elements from a linked list of integers that have value <b><i>val</i></b>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>  1-&gt;2-&gt;6-&gt;3-&gt;4-&gt;5-&gt;6, <em><b>val</b></em> = 6
<b>Output:</b> 1-&gt;2-&gt;3-&gt;4-&gt;5
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        
        ListNode* next = nullptr;
        
        while (head) {
            next = head->next;
            if (head->val != val) {
                tail->next = head;
                tail = tail->next;
                tail->next = nullptr;
            }
            head = next;
        }
        
        return dummy->next;
    }
};
```
