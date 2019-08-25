# 61. Rotate List

* *Difficulty: Medium*

* *Topics: Linked List, Two Pointers*

* *Similar Questions:*

  * [Rotate Array](rotate-array.md)

  * [Split Linked List in Parts](split-linked-list-in-parts.md)

## Problem:

<p>Given a linked&nbsp;list, rotate the list to the right by <em>k</em> places, where <em>k</em> is non-negative.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL, k = 2
<strong>Output:</strong> 4-&gt;5-&gt;1-&gt;2-&gt;3-&gt;NULL
<strong>Explanation:</strong>
rotate 1 steps to the right: 5-&gt;1-&gt;2-&gt;3-&gt;4-&gt;NULL
rotate 2 steps to the right: 4-&gt;5-&gt;1-&gt;2-&gt;3-&gt;NULL
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 0-&gt;1-&gt;2-&gt;NULL, k = 4
<strong>Output:</strong> <code>2-&gt;0-&gt;1-&gt;NULL</code>
<strong>Explanation:</strong>
rotate 1 steps to the right: 2-&gt;0-&gt;1-&gt;NULL
rotate 2 steps to the right: 1-&gt;2-&gt;0-&gt;NULL
rotate 3 steps to the right:&nbsp;<code>0-&gt;1-&gt;2-&gt;NULL</code>
rotate 4 steps to the right:&nbsp;<code>2-&gt;0-&gt;1-&gt;NULL</code></pre>

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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL)   return NULL;
        int count = 1;
        ListNode* cur = head;
        
        while (cur->next) {
            ++count;
            cur = cur->next;
        }
        cur->next = head;
        
        k = k % count;
        
        cur = head;
        for (int i = 0; i < (count - k - 1); ++i) {
            cur = cur->next;
        }
        
        ListNode* ret = cur->next;
        cur->next = NULL;
        return ret;
        
    }
};
```
