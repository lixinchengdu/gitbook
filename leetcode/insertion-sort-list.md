# 147. Insertion Sort List

* *Difficulty: Medium*

* *Topics: Linked List, Sort*

* *Similar Questions:*

  * [Sort List](sort-list.md)

  * [Insert into a Cyclic Sorted List](insert-into-a-cyclic-sorted-list.md)

## Problem:

<p>Sort a linked list using insertion sort.</p>

<ol>
</ol>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" style="height:180px; width:300px" /><br />
<small>A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.<br />
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list</small><br />
&nbsp;</p>

<ol>
</ol>

<p><strong>Algorithm of Insertion Sort:</strong></p>

<ol>
	<li>Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.</li>
	<li>At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.</li>
	<li>It repeats until no input elements remain.</li>
</ol>

<p><br />
<strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 4-&gt;2-&gt;1-&gt;3
<strong>Output:</strong> 1-&gt;2-&gt;3-&gt;4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -1-&gt;5-&gt;3-&gt;4-&gt;0
<strong>Output:</strong> -1-&gt;0-&gt;3-&gt;4-&gt;5
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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        while (head) {
            ListNode* next = head->next;
            insert(dummy, head);
            head = next;
        }
        
        return dummy->next;
    }
    
    void insert(ListNode* head, ListNode* cur) {
        while (head->next && head->next->val < cur->val)    head = head->next;
        if (head->next == nullptr) {
            head->next = cur;
            cur->next = nullptr;
        } else {
            cur->next = head->next;
            head->next = cur;
        } 
    }
};
```
