# 2. Add Two Numbers

* *Difficulty: Medium*

* *Topics: Linked List, Math*

* *Similar Questions:*

  * [Multiply Strings](multiply-strings.md)

  * [Add Binary](add-binary.md)

  * [Sum of Two Integers](sum-of-two-integers.md)

  * [Add Strings](add-strings.md)

  * [Add Two Numbers II](add-two-numbers-ii.md)

  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)

## Problem:

<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b> and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> (2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<b>Output:</b> 7 -&gt; 0 -&gt; 8
<b>Explanation:</b> 342 + 465 = 807.
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* cur = head;
        int carry = 0;
       
        while (l1 != NULL || l2 != NULL) {
            int val1 = 0;
            int val2 = 0;
            if (l1) {
                val1 = l1->val;
                l1 = l1->next;
            } 
            if (l2) {
                val2 = l2->val;
                l2 = l2->next;
            }
            
            int sum = val1 + val2 + carry;
            carry = sum/10;
            cur->next = new ListNode(sum%10);
            cur = cur->next;
        }
        
        if (carry == 1) {
            cur->next = new ListNode(1);
        }
        
        return head->next;
    }
};
```

## Another More Solution

This solution breaks the while loop earlier to avoid unnecessary list traversal. 

```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* cur = head;
        int carry = 0;
       
        while (carry == 1 || (l1 != NULL && l2 != NULL)) {
            int val1 = 0;
            int val2 = 0;
            if (l1) {
                val1 = l1->val;
                l1 = l1->next;
            } 
            if (l2) {
                val2 = l2->val;
                l2 = l2->next;
            }
            
            int sum = val1 + val2 + carry;
            carry = sum/10;
            cur->next = new ListNode(sum%10);
            cur = cur->next;
        }
        
        if (l1 != NULL) {
            cur->next = l1;
        } else {
            cur->next = l2;
        }
        
        return head->next;
    }
};
```
