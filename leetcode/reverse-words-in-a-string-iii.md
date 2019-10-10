# 557. Reverse Words in a String III

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Reverse String II](reverse-string-ii.md)

## Problem:

<p>Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "Let's take LeetCode contest"
<b>Output:</b> "s'teL ekat edoCteeL tsetnoc"
</pre>
</p>

<p><b>Note:</b>
In the string, each word is separated by single space and there will not be any extra space in the string.
</p>
## Solutions:

```c++
class Solution {
public:
    string reverseWords(string s) {
        int pos = 0;
        while (pos < s.length()) {
            int left = pos;
            int right = left;
            while (right < s.length() && s[right] != ' ') ++right;
            pos = right + 1;
            right = right - 1;
            
            while (left < right) {
                swap(s[left], s[right]);
                ++left;
                --right;
            }
        }
        
        return s;
    }
};
```
