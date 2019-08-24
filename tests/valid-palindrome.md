# 125. Valid Palindrome

* *Difficulty: Easy*

* *Topics: Two Pointers, String*

* *Similar Questions:*

  * [Palindrome Linked List](./tests/valid-palindrome.md)

  * [Valid Palindrome II](./tests/valid-palindrome.md)

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
    char toLowerCase (char c) {
        return c >= 'A' && c <= 'Z' ? 'a' + c - 'A' : c;
    }
    
    bool isAlphabeticNum (char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
    }
    
    bool isSameChar (char c, char t) {
        
        return toLowerCase(c) == toLowerCase(t);
    }
    
    
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            while (left < s.length() && !isAlphabeticNum(s[left])) left++;
            while (right >= 0 && !isAlphabeticNum(s[right]))    right --;
            //cout << s[left] << ": " << s[right] << endl;
            //cout << abs(s[left] - s[right]) << endl;
            if (!isSameChar(s[left], s[right])) return false;
            else {
                left ++;
                right --;
            }
        }
        return true;
    }
};
```
