# 504. Base 7

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Given an integer, return its base 7 string representation.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 100
<b>Output:</b> "202"
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> -7
<b>Output:</b> "-10"
</pre>
</p>

<p><b>Note:</b>
The input will be in range of [-1e7, 1e7].
</p>
## Solutions:

```c++
class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0)   return "0";
        int sign = 1;
        if (num < 0) {
            sign = -1;
            num = -num;
        }
        
        string ret;
        while (num > 0) {
            ret.push_back('0' + num % 7);
            num /= 7;
        }
        
        if (sign == -1) {
            ret.push_back('-');
        }
        
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```
