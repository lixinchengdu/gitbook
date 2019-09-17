# 835. Linked List Components

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

## Problem:

<p>We are given&nbsp;<code>head</code>,&nbsp;the head node of a linked list containing&nbsp;<strong>unique integer values</strong>.</p>

<p>We are also given the list&nbsp;<code>G</code>, a subset of the values in the linked list.</p>

<p>Return the number of connected components in <code>G</code>, where two values are connected if they appear consecutively in the linked list.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3
G = [0, 1, 3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3-&gt;4
G = [0, 3, 1, 4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li>If&nbsp;<code>N</code>&nbsp;is the&nbsp;length of the linked list given by&nbsp;<code>head</code>,&nbsp;<code>1 &lt;= N &lt;= 10000</code>.</li>
	<li>The value of each node in the linked list will be in the range<code> [0, N - 1]</code>.</li>
	<li><code>1 &lt;= G.length &lt;= 10000</code>.</li>
	<li><code>G</code> is a subset of all values in the linked list.</li>
</ul>

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
    int numComponents(ListNode* head, vector<int>& G) {
        unordered_set<int> nums(G.begin(), G.end());
        ListNode* cur = head;
        int ret = 0;
        bool hasNum = false;
        while (cur) {
            if (nums.count(cur->val) == 0) {
                if (hasNum) {
                    ++ret;
                    hasNum = false;
                }
                cur = cur->next;
            } else {
                hasNum = true;
                cur = cur->next;
            }
        }
        
        if (hasNum) {
            ++ret;
        }
        
        return ret;
    }
};
```
