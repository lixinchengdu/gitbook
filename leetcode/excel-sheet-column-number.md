# 171. Excel Sheet Column Number

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Excel Sheet Column Title](excel-sheet-column-title.md)

## Problem:

<p>Given a column title as appear in an Excel sheet, return its corresponding column number.</p>

<p>For example:</p>

<pre>
    A -&gt; 1
    B -&gt; 2
    C -&gt; 3
    ...
    Z -&gt; 26
    AA -&gt; 27
    AB -&gt; 28 
    ...
</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;A&quot;
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;AB&quot;
<strong>Output:</strong> 28
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;ZY&quot;
<strong>Output:</strong> 701
</pre>
## Solutions:

```c++
class Solution {
public:
    int titleToNumber(string s) {
        int ret = 0;
        for (int i = 0; i < s.length(); ++i) {
            ret = 26 * ret + (s[i] - 'A' + 1); // be careful about overflow
        }
        
        return ret;
    }
};
```
