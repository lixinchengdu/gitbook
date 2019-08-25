# 9. Palindrome Number

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Palindrome Linked List](palindrome-linked-list.md)

## Problem:

<p>Determine whether an integer is a palindrome. An integer&nbsp;is&nbsp;a&nbsp;palindrome when it&nbsp;reads the same backward as forward.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 121
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p><strong>Follow up:</strong></p>

<p>Coud you solve&nbsp;it without converting the integer to a string?</p>

## Solutions:

```c++
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)  return false;
        int reverse = 0;
        int val = x;
        while (val > 0) {
            int digit = val % 10;
            val = val/10;
            if (reverse > INT_MAX/10 || reverse == INT_MAX/10 && digit > INT_MAX % 10)  return false; // remember to check overflow!
            reverse = 10 * reverse + digit;
        }
        
        return reverse == x;
    }
};
```
