# 6. ZigZag Conversion

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows =&nbsp;4
<strong>Output:</strong>&nbsp;&quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>

P     I    N
A   L S  I G
Y A   H R
P     I</pre>

## Solutions:

```c++
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 0)    return "";
        if (numRows == 1)   return s;
        int period = 2 * (numRows - 1);
        string ret;
        for (int row = 0; row < numRows; ++row) {
            for (int i = row; i < s.length(); i = i + period) {
                ret.push_back(s[i]);
                if (row != 0 && row != numRows - 1 && i + (numRows - 1 - row) * 2 < s.length()) {
                    ret.push_back(s[i + (numRows - 1 - row) * 2]);
                }
            }
        }
        
        return ret;
    }
};
```

### More intuitive solution
Use multiple strings.

From [https://www.cnblogs.com/grandyang/p/4128268.html]Grandyang:
```c++
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) return s;
        string res;
        int i = 0, n = s.size();
        vector<string> vec(numRows);
        while (i < n) {
            for (int pos = 0; pos < numRows && i < n; ++pos) {
                vec[pos] += s[i++];
            }
            for (int pos = numRows - 2; pos >= 1 && i < n; --pos) {
                vec[pos] += s[i++];
            }
        }
        for (auto &a : vec) res += a;
        return res;
    }
};
```
