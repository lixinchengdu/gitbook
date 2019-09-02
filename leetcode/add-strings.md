# 415. Add Strings

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Add Two Numbers](add-two-numbers.md)

  * [Multiply Strings](multiply-strings.md)

  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)

## Problem:

<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as string, return the sum of <code>num1</code> and <code>num2</code>.</p>

<p><b>Note:</b>
<ol>
<li>The length of both <code>num1</code> and <code>num2</code> is < 5100.</li>
<li>Both <code>num1</code> and <code>num2</code> contains only digits <code>0-9</code>.</li>
<li>Both <code>num1</code> and <code>num2</code> does not contain any leading zero.</li>
<li>You <b>must not use any built-in BigInteger library</b> or <b>convert the inputs to integer</b> directly.</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    string addStrings(string num1, string num2) {
        string ret;
        int carry = 0;
        int i1 = num1.length() - 1;
        int i2 = num2.length() - 1; 
        
        while (carry != 0 || i1 >= 0 && i2 >= 0) {
            int value = carry + (i1 >= 0 ? num1[i1--] - '0': 0) + (i2 >= 0 ? num2[i2--] - '0' : 0);
            ret.push_back(value % 10 + '0');
            carry = value / 10;
        }
        
        reverse(ret.begin(), ret.end());
        
        if (i1 >= 0) {
            ret = num1.substr(0, i1 + 1) + ret;
        }
        
        if (i2 >= 0) {
            ret = num2.substr(0, i2 + 1) + ret;
        }
        
        return ret;
        
    }
};
```
