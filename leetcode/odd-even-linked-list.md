# 328. Odd Even Linked List

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

  * [Split Linked List in Parts](split-linked-list-in-parts.md)

## Problem:

<p>Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.</p>

<p>You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong><code>1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL</code>
<strong>Output: </strong><code>1-&gt;3-&gt;5-&gt;2-&gt;4-&gt;NULL</code>
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong>2<code>-&gt;1-&gt;3-&gt;5-&gt;6-&gt;4-&gt;7-&gt;NULL</code>
<strong>Output: </strong><code>2-&gt;3-&gt;6-&gt;7-&gt;1-&gt;5-&gt;4-&gt;NULL</code>
</pre>

<p><b>Note:</b></p>

<ul>
	<li>The relative order inside both the even and odd groups should remain as it was in the input.</li>
	<li>The first node is considered odd, the second node even and so on ...</li>
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
    ListNode* oddEvenList(ListNode* head) {
        ListNode* evenDummyHead = new ListNode(0);
        ListNode* oddDummyHead = new ListNode(0);
        
        ListNode* evenCur = evenDummyHead;
        ListNode* oddCur = oddDummyHead;
        ListNode* cur = head;
        int count = 0;
        
        while (cur) {
            if (count % 2 == 0) {
                evenCur->next = cur;
                evenCur = evenCur->next;
            } else {
                oddCur->next = cur;
                oddCur = oddCur->next;
            }
            
            cur = cur->next;
            ++count;
        }
        
        evenCur->next = oddDummyHead->next;
        oddCur->next = NULL;
        
        return evenDummyHead->next;
    }
};
```
