# 43. Multiply Strings

* *Difficulty: Medium*

* *Topics: Math, String*

* *Similar Questions:*

  * [Add Two Numbers](./tests/multiply-strings.md)

  * [Plus One](./tests/multiply-strings.md)

  * [Add Binary](./tests/multiply-strings.md)

  * [Add Strings](./tests/multiply-strings.md)

## Problem:

<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;2&quot;, num2 = &quot;3&quot;
<strong>Output:</strong> &quot;6&quot;</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;123&quot;, num2 = &quot;456&quot;
<strong>Output:</strong> &quot;56088&quot;
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The length of both <code>num1</code> and <code>num2</code> is &lt; 110.</li>
	<li>Both <code>num1</code> and <code>num2</code> contain&nbsp;only digits <code>0-9</code>.</li>
	<li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number 0 itself.</li>
	<li>You <strong>must not use any built-in BigInteger library</strong> or <strong>convert the inputs to integer</strong> directly.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    string multiply(string num1, string num2) {
        int n1 = num1.length();
        int n2 = num2.length();
        string result;
        if (!n1 || !n2) return result;
        result = string(n1+n2, '0');
        for (int i = n1 - 1; i >= 0; i--)
        {
            for (int j = n2 -1; j >= 0; j--)
            {
                int unitDigit = (num1[i]-'0')*(num2[j]-'0')%10;
                int tenDigit = (num1[i] - '0') * (num2[j] - '0')/10;
                int resultIndex = n1 + n2 - 1 - ((n1-1) - i + (n2-1) - j);
                //cout << resultIndex << endl;
                result[resultIndex] += unitDigit;
                result[resultIndex-1] += tenDigit;
                if (result[resultIndex] > '9')
                {
                    result[resultIndex] -= 10;
                    result[resultIndex-1] += 1;
                }
               // result[resultIndex-1] += tenDigit;
                if (result[resultIndex-1] > '9')
                {
                    result[resultIndex-1] -= 10;
                    result[resultIndex-2] += 1;
                }
            }
        }
        int start = 0;
        while (start < result.length() && result[start] == '0')    start++;
        if (start == result.length())   return "0";
        return result[0] == '0'? result.substr(start) : result;
        
    }
};
```
