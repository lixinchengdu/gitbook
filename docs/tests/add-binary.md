# 67. Add Binary

* *Difficulty: Easy*

* *Topics: Math, String*

* *Similar Questions:*

  * [Add Two Numbers](./tests/add-binary.md)

  * [Multiply Strings](./tests/add-binary.md)

  * [Plus One](./tests/add-binary.md)

  * [Add to Array-Form of Integer](./tests/add-binary.md)

## Problem:

<p>Given two binary strings, return their sum (also a binary string).</p>

<p>The input strings are both <strong>non-empty</strong> and contains only characters <code>1</code> or&nbsp;<code>0</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = &quot;11&quot;, b = &quot;1&quot;
<strong>Output:</strong> &quot;100&quot;</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = &quot;1010&quot;, b = &quot;1011&quot;
<strong>Output:</strong> &quot;10101&quot;</pre>

## Solutions:

```c++
class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int carry = 0;
        int n1 = a.length() -1;
        int n2 = b.length() -1;
        while (n1 >= 0 || n2 >= 0)
        {
            int val1 = 0;
            int val2 = 0;
            if (n1 >= 0)    val1 = a[n1] - '0';
            if (n2 >= 0)    val2 = b[n2] - '0';
            int sum = val1 + val2 + carry;
            
            //int sum = (a[n1] - '0') + (a[n2] - '0') + carry;
            result = string(1, sum%2+'0') + result;
            carry = sum/2;
            n1 --;
            n2 --;
        }
        if (carry == 1)
            result = string(1, '1') + result;
        return result == ""? "0": result;
    }
};
```
