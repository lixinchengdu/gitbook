# 434. Number of Segments in a String

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.</p>

<p>Please note that the string does not contain any <b>non-printable</b> characters.</p>

<p><b>Example:</b></p>
<pre>
<b>Input:</b> "Hello, my name is John"
<b>Output:</b> 5
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int countSegments(string s) {
        if (s.length() == 0)    return 0;
        int pos = 1;
        int count = (s[0] == ' ' ? 0 : 1);
        while (pos < s.length()) {
            if (s[pos] != ' ' && s[pos-1] == ' ')   ++count;
            ++pos;
        }
        return count;
    }
};
```
