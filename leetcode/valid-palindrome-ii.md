# 680. Valid Palindrome II

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Valid Palindrome](valid-palindrome.md)

## Problem:

<p>
Given a non-empty string <code>s</code>, you may delete <b>at most</b> one character.  Judge whether you can make it a palindrome.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aba"
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "abca"
<b>Output:</b> True
<b>Explanation:</b> You could delete the character 'c'.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    bool validPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return isPanlindrome(s, left + 1, right) || isPanlindrome(s, left, right - 1);
            }
            ++left;
            --right;
        }
        
        return true;
    }
    
private:
    bool isPanlindrome(string& s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right])    return false;
            ++left;
            --right;
        }
        
        return true;
    }
};
```
