# 234. Palindrome Linked List

* *Difficulty: Easy*

* *Topics: Linked List, Two Pointers*

* *Similar Questions:*

  * [Palindrome Number](palindrome-number.md)

  * [Valid Palindrome](valid-palindrome.md)

  * [Reverse Linked List](reverse-linked-list.md)

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
        ListNode* mid = middlePoint(head);
        ListNode* half = reverse(mid);
        
        //cout << mid->val << endl;
        //cout << half->val << endl;
        
        while (half) {
            //cout << head->val << " " << half->val << endl;
            if (head->val != half->val)  return false;
            head = head->next;
            half = half->next;
        }
        return true;
    }
    
    ListNode* middlePoint(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast -> next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        return slow;
    }
    
    ListNode* reverse(ListNode* head) {
        if (head == NULL)   return NULL;
        ListNode* dummy = new ListNode(0);
        ListNode* cur = head;
        ListNode* next = NULL;
        while (cur) {
            next = cur->next;
            cur->next = dummy->next;
            dummy->next = cur;
            cur = next;
        }
        return dummy->next;
    }
};
```
