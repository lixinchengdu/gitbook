# 234. Palindrome Linked List

* *Difficulty: Easy*

* *Topics: Linked List, Two Pointers*

* *Similar Questions:*

  * [Palindrome Number](./tests/palindrome-linked-list.md)

  * [Valid Palindrome](./tests/palindrome-linked-list.md)

  * [Reverse Linked List](./tests/palindrome-linked-list.md)

## Problem:

<p>Given a singly linked list, determine if it is a palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;2-&gt;1
<strong>Output:</strong> true</pre>

<p><b>Follow up:</b><br />
Could you do it in O(n) time and O(1) space?</p>

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
    bool isPalindrome(ListNode* head) {
        if (!head)  return true;
        if (!head -> next)  return true;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast -> next)
        {
            slow = slow -> next;
            fast = fast -> next -> next;
        }
        
        ListNode* tailHead = revertList(slow);
        ListNode* cur_tail = tailHead;
        ListNode* cur_head = head;
        while (cur_head && cur_tail)
        {
            if (cur_tail -> val != cur_head -> val) return false;
            cur_tail = cur_tail -> next;
            cur_head = cur_head -> next;
        }
        return true;
        
        
    }
    
    ListNode* revertList(ListNode* head)
    {
        ListNode* current = head;
        ListNode* previous = NULL;
        ListNode* current_next = NULL;
        ListNode* previous_next = NULL;
        
        if (!head)  return NULL;
        
        while(current)
        {
            current_next = current -> next;
            previous_next = current;
            current -> next = previous;
            current = current_next;
            previous = previous_next;
        }
        
        return previous;
    }
    
};
```
