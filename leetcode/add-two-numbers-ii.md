# 445. Add Two Numbers II

* *Difficulty: Medium*

* *Topics: Linked List*

* *Similar Questions:*

  * [Add Two Numbers](add-two-numbers.md)

## Problem:

<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Follow up:</b><br />
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
</p>

<p>
<b>Example:</b>
<pre>
<b>Input:</b> (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
<b>Output:</b> 7 -> 8 -> 0 -> 7
</pre>
</p>
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> stk1, stk2, ret;
        
        while (l1) {
            stk1.push(l1->val);
            l1 = l1 -> next;
        }
        
        while (l2) {
            stk2.push(l2->val);
            l2 = l2 -> next;
        }
        
        int carry = 0;
        
        while (carry != 0 || !stk1.empty() && !stk2.empty()) {
            int val = carry + (stk1.empty() ? 0 : stk1.top()) + (stk2.empty() ? 0 : stk2.top());
            if (!stk1.empty()) stk1.pop(); 
            if (!stk2.empty()) stk2.pop();
            ret.push(val % 10);
            carry = val / 10;
        }
        
        while (!stk1.empty()) {
            ret.push(stk1.top()); stk1.pop();
        }
        
        while(!stk2.empty()) {
            ret.push(stk2.top()); stk2.pop();
        }
        
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        while (!ret.empty()) {
            tail -> next = new ListNode(ret.top()); ret.pop();
            tail = tail->next;
        }                     
        
        return dummy->next;
    }
};
```
