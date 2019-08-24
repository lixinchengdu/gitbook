# 168. Excel Sheet Column Title

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Excel Sheet Column Number](./tests/excel-sheet-column-title.md)

## Problem:

<p>Given a positive integer, return its corresponding column title as appear in an Excel sheet.</p>

<p>For example:</p>

<pre>
    1 -&gt; A
    2 -&gt; B
    3 -&gt; C
    ...
    26 -&gt; Z
    27 -&gt; AA
    28 -&gt; AB 
    ...
</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 28
<strong>Output:</strong> &quot;AB&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 701
<strong>Output:</strong> &quot;ZY&quot;
</pre>
## Solutions:

```c++
class Solution {
public:
    string convertToTitle(int n) {
        string result;
        while (n > 0)
        {
            int r = (n-1)%26;
            result = string(1, r  + 'A') + result;
            n -= (r+1);
            n /= 26;
        }
        return result;
        
    }
};
```
