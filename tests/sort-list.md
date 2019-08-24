# 148. Sort List

* *Difficulty: Medium*

* *Topics: Linked List, Sort*

* *Similar Questions:*

  * [Merge Two Sorted Lists](./tests/sort-list.md)

  * [Sort Colors](./tests/sort-list.md)

  * [Insertion Sort List](./tests/sort-list.md)

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
ListNode* MergeSort (ListNode* head);
ListNode* Merge(ListNode* half1, ListNode* half2);
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        MergeSort (head);
    }
};


ListNode* MergeSort (ListNode* head)
{
    if (head == NULL) return NULL;
    if (head -> next == NULL)   return head;
    int counter = 0;
        ListNode* it = head;
        ListNode* mid = head;
        while (it->next)
        {
            it = it->next;
            counter++;
            if (!((counter)%2)) mid = mid->next;
        }
        cout << counter << ";";
        ListNode* half2 = MergeSort(mid->next);
        mid->next = NULL;
        ListNode* half1 = MergeSort(head);
        return Merge (half1, half2);
}

ListNode* Merge(ListNode* half1, ListNode* half2)
{
    ListNode* head = NULL;
    ListNode* tail = NULL;
    if (!half1) return half2;
    if (!half2) return half1;
    if (half1 -> val <= half2 -> val)
    {
        head = half1;
        half1 = half1 -> next;
    }
    else
    {
        head = half2;
        half2 = half2 -> next;
    }
   tail = head;
    while (half1 && half2 )
    {
        if (half1 -> val <= half2 -> val)
        {
            tail -> next = half1;
            half1 = half1 -> next;
            tail = tail -> next;
        }
        else 
        {
            tail -> next = half2;
            half2 = half2 -> next;
            tail = tail-> next;
        }
    }
    if (!half1) tail->next = half2;
    else tail-> next = half1;
    return head;
}
```
