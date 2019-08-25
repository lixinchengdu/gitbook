# 67. Add Binary

* *Difficulty: Easy*

* *Topics: Math, String*

* *Similar Questions:*

  * [Add Two Numbers](add-two-numbers.md)

  * [Multiply Strings](multiply-strings.md)

  * [Plus One](plus-one.md)

  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)

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
        string ret;
        int carry = 0;
        int indexA = a.length() - 1;
        int indexB = b.length() - 1;
     
        while (indexA >= 0 || indexB >= 0) {
            int digitA = 0;
            int digitB = 0;
            if (indexA >= 0) {
                digitA = a[indexA--] - '0';
            }
            
            if (indexB >= 0) {
                digitB = b[indexB--] - '0';
            }
            
            int val = carry + digitA + digitB;
            ret.push_back('0' + val%2);
            carry = val/2;
        }
        
        if (carry == 1) ret.push_back('1');
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```
