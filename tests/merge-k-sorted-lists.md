# 23. Merge k Sorted Lists

* *Difficulty: Hard*

* *Topics: Linked List, Divide and Conquer, Heap*

* *Similar Questions:*

  * [Merge Two Sorted Lists](./tests/merge-k-sorted-lists.md)

  * [Ugly Number II](./tests/merge-k-sorted-lists.md)

## Problem:

<p>Merge <em>k</em> sorted linked lists and return it as one sorted list. Analyze and describe its complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; 1-&gt;4-&gt;5,
&nbsp; 1-&gt;3-&gt;4,
&nbsp; 2-&gt;6
]
<strong>Output:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)  return NULL;
        else if (lists.size() == 1)  return lists[0];
        else
        {
            int halfSize = lists.size()/2;
            vector <ListNode*> firstHalf (lists.begin(), lists.begin()+halfSize);
            vector <ListNode*> secondHalf (lists.begin()+halfSize, lists.end());
            ListNode* first = mergeKLists(firstHalf);
            ListNode* second = mergeKLists(secondHalf);
            ListNode* previousNode = NULL;
            ListNode* headNode = NULL;
            while (first && second)
            {
                if (first -> val <= second -> val)  
                {
                    if (previousNode)
                    {
                        previousNode -> next = first;
                    }
                    else
                    {
                        headNode = first;
                    }
                    previousNode = first;
                    first = first -> next;
                }
                else
                {
                    if (previousNode)
                    {
                        previousNode -> next = second;
                    }
                    else
                    {
                        headNode = second;
                    }
                    previousNode = second;
                    second = second -> next;
                }
            }
            if (first)
            {
                if (previousNode)
                    previousNode -> next = first;
                else
                {
                    headNode = first;
                }
            }
            if (second)
            {
                if (previousNode)
                    previousNode -> next = second;
                else
                {
                    headNode = second;
                }
            }
         
            return headNode;   
        }
        
        
    }
};
```
