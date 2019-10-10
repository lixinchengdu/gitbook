# 541. Reverse String II

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Reverse String](reverse-string.md)

  * [Reverse Words in a String III](reverse-words-in-a-string-iii.md)

## Problem:

</p>
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> s = "abcdefg", k = 2
<b>Output:</b> "bacdfeg"
</pre>
</p>

<b>Restrictions:</b> </b>
<ol>
<li> The string consists of lower English letters only.</li>
<li> Length of the given string and k will in the range [1, 10000]</li>
</ol>
## Solutions:

```c++
class Solution {
public:
    string reverseStr(string s, int k) {
        int pos = 0;
        while (pos < s.length()) {
            int left = pos;
            int right = min(pos + k - 1, (int) s.length() - 1);
            while (left < right) {
                swap(s[left], s[right]);
                ++left;
                --right;
            }
            pos += 2 * k;
        }
        
        return s;
    }
};
```
