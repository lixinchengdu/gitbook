# 2. Add Two Numbers

* *Difficulty: Medium*

* *Topics: Linked List, Math*

* *Similar Questions:*

  * [Multiply Strings](./tests/add-two-numbers.md)

  * [Add Binary](./tests/add-two-numbers.md)

  * [Sum of Two Integers](./tests/add-two-numbers.md)

  * [Add Strings](./tests/add-two-numbers.md)

  * [Add Two Numbers II](./tests/add-two-numbers.md)

  * [Add to Array-Form of Integer](./tests/add-two-numbers.md)

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
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    head := &ListNode{}
    cur := head
    carry := 0
    for l1 != nil || l2 != nil || carry > 0 {
        sum := carry
        if l1 != nil {
            sum = sum + l1.Val
            l1 = l1.Next
        }
        
        if l2 != nil {
            sum = sum + l2.Val
            l2 = l2.Next
        }
        
        carry = sum / 10
        cur.Next = &ListNode{Val : sum % 10}
        cur = cur.Next
    }
    
    return head.Next
}
```
