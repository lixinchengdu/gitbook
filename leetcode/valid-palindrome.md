# 125. Valid Palindrome

* *Difficulty: Easy*

* *Topics: Two Pointers, String*

* *Similar Questions:*

  * [Palindrome Linked List](palindrome-linked-list.md)

  * [Valid Palindrome II](valid-palindrome-ii.md)

## Problem:

<p>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.</p>

<p><strong>Note:</strong>&nbsp;For the purpose of this problem, we define empty string as valid palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;race a car&quot;
<strong>Output:</strong> false
</pre>

## Solutions:

```c++
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
    
        while (left < right) {
            while (left < right && !isalphanum(s[left])) {
                ++left;
            }
        
            while (left < right && !std::isalnum(s[right])){ // remember the name of the funciton
                --right;
            }
            
            if (s[left] >= '0' && s[left] <= '9' && s[left] != s[right]) {
                return false;
            }
            
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            
            
            ++left;
            --right;
        }
        
        return true;
    }
    
    bool isalphanum(char c) {
        return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c >= '0' && c <= '9';
    }
    
};
```
