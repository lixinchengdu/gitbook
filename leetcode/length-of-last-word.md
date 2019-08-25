# 58. Length of Last Word

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Given a string <i>s</i> consists of upper/lower-case alphabets and empty space characters <code>&#39; &#39;</code>, return the length of last word in the string.</p>

<p>If the last word does not exist, return 0.</p>

<p><b>Note:</b> A word is defined as a character sequence consists of non-space characters only.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> &quot;Hello World&quot;
<b>Output:</b> 5
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != ' ') {
                if (i != 0 && s[i-1] == ' ') len = 1;
                else ++len;
            }
        }
        return len;
    }
};
```
